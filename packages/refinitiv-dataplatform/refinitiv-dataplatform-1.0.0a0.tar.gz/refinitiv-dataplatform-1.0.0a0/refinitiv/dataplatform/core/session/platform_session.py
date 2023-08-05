# coding: utf-8

__all__ = ["PlatformSession"]

import logging
import asyncio
import nest_asyncio
import requests_async as requests
from threading import Timer, Thread, Event
from .session import Session, DacsParams
from .elektronError import ElektronError
from .grant import Grant
from .grant_refresh import GrantRefreshToken
from .grant_password import GrantPassword


# Load nest_asyncio to allow multiple calls to run_until_complete available
nest_asyncio.apply()


class PlatformSession(Session):
    """
    The EDPSession specification details the properties specific to the Elektron Data Platform (EDP).
    Properties include how an EDP user is authenticated when accessing content from the platform.
    """

    # Authorization endpoint used to authenticate within the Elektron Data Core(EDP).
    AuthEndpoint = u"https://api.refinitiv.com/auth/oauth2/beta1/token"

    # Root endpoint to discover stream services within the Elektron Data Core (EDP).
    StreamDiscoveryEndpoint = u"https://api.refinitiv.com/streaming/pricing/beta1/"

    # u"https://api.edp.thomsonreuters.com/streaming/pricing/v1/?dataformat=tr_json2"

    class RefreshTokenThread(Thread):
        def __init__(self, session, delay):
            super().__init__()
            self._cancel_event = Event()
            self._session = session
            self._delay = delay
            self._loop = None
            self._http_session = requests.sessions.Session()

        def run(self):
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)
            while not self._cancel_event.is_set():
                pooling_delay = 0
                while pooling_delay < self._delay and not self._cancel_event.is_set():
                    self._loop.run_until_complete(asyncio.sleep(1))
                    pooling_delay += 1
                if not self._cancel_event.is_set():
                    self._refresh_token()

        def cancel(self):
            self._cancel_event.set()

        def _refresh_token(self):
            """
            Manages the EDP token refresh task based on OAuth requirements.
            This handler gets called every N minutes, based on the authorization response from EDP.
            The goal here is to refresh the access token required to requests for stream and non-stream data.
            """
            try:
                _refresh_token_task = self._request_refresh_token(self._session._refresh_grant)
                _response = self._loop.run_until_complete(_refresh_token_task)

                if _response is None:
                    raise requests.exceptions.ConnectionError("Refresh token request failed, response is None")

                # Process the Refresh Token response
                if self._check_token_response(_response):
                    # forward token to web socket
                    if self._session._streaming_session:
                        self._session._streaming_session.refresh_token(self._session._access_token)

            except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as error:
                self._session.logger().warn(f"EDP Token Refresh failed : {str(error)}")

        async def _request_refresh_token(self, grant):
            if grant is None:
                raise ElektronError(-1, "AuthorizeUser is passed a null grant")
            _post_data = {
                "client_id": self._session.app_key,
                "grant_type": "refresh_token",
                "username": grant.get_username(),
                "refresh_token": grant.get_refresh_token(),
                "takeExclusiveSignOnControl": True
            }

            self._session.log(logging.DEBUG, "Send refresh token to {}"
                     .format(PlatformSession.AuthEndpoint))
            self._session.log(1, "   with post data {}\n   with auth {}"
                     .format(str(_post_data), str((grant.get_username(), ""))))

            _response = await self.http_request_async(method="POST",
                                                      url=PlatformSession.AuthEndpoint,
                                                      headers={"Accept": "application/json"},
                                                      data=_post_data,
                                                      auth=(grant.get_username(), ""))

            if _response is not None:
                self._session.log(logging.DEBUG, "Refresh token response: {}".format(_response.text))
            else:
                self._session.log(logging.ERROR, "Refresh token failed, response is None")

            return _response

        def _check_token_response(self, response):
            if response is None:
                raise requests.exceptions.HTTPError("Response is None")

            if response.status_code != requests.codes.ok:
                # Looks like authentication failed.  Report an error
                self._session._status = Session.EventCode.SessionAuthenticationFailed
                self._session._last_event_code = Session.EventCode.SessionAuthenticationFailed
                self._session._last_event_message = response.json().get("error_description")
                try:
                    _json = response.json()
                except ValueError:
                    _json = None
                if _json:
                    _error = _json.get("error")
                    _description = _json.get("error_description")
                    self._session.log(logging.ERROR,
                             f"[Error {response.status_code} - {_error}] {_description}")
                self._session._on_event(self, self._session._last_event_code, self._session._last_event_message)
                return False

            self._status = Session.EventCode.SessionAuthenticationSuccess

            # Process the Authentication response
            _json_response = response.json()
            self._session._refresh_grant.refresh_token(_json_response["refresh_token"])
            self._session._access_token = _json_response["access_token"]
            self._session._token_expiry_in_secs = _json_response["expires_in"]
            return True

        async def http_request_async(self, url: str, method=None, headers={},
                                     data=None, params=None, json=None, auth=None,
                                     loop=None, **kwargs):
            if method is None:
                method = "GET"

            if self._session._access_token is not None:
                headers["Authorization"] = f"Bearer {self._session._access_token}"

            _http_request = requests.Request(method, url, headers=headers, data=data, params=params, json=json, auth=auth, **kwargs)
            _prepared_request = _http_request.prepare()

            self._session.log(logging.DEBUG,
                f"Request to {_prepared_request.url}\n   headers = {_prepared_request.headers}\n   params = {kwargs.get('params')}")
            try:
                _request_response = await self._http_session.send(_prepared_request, **kwargs)
                self._session.log(1, f"HTTP request response : HTTP {_request_response.status_code} - {_request_response.text}")
                return _request_response
            except Exception as e:
                self._session.log(1, f"HTTP request failed: {e!r}")

            return None

    class Params(Session.Params):
        def __init__(self, *args, **kwargs):
            super(PlatformSession.Params, self).__init__(*args, **kwargs)

            self._grant = kwargs.get("grant")
            _signon_control = kwargs.get("signon_control", "False")
            self._take_signon_control = _signon_control.lower() == "true"

            if self._take_signon_control is None:
                self._take_signon_control = False

        def get_grant(self):
            return self._grant

        def grant_type(self, grant):
            if isinstance(grant, Grant):
                self._grant = grant
            else:
                raise Exception("wrong Elektron authentication parameter")
            return self

        def take_signon_control(self):
            return self._take_signon_control

        def with_take_signon_control(self, value):
            if value is not None:
                self._take_signon_control = value
            return self

    def get_session_params(self):
        return self._session_params

    def session_params(self, session_params):
        self._session_params = session_params
        return session_params

    def _get_rdp_url_root(self):
        return u"https://api.refinitiv.com"

    def __init__(self, app_key=None, grant=None, signon_control=None, **kwargs):
        super().__init__(app_key, **kwargs)

        self._ws_endpoints = []
        if grant and isinstance(grant, GrantPassword):
            self._grant = grant
        else:
            raise AttributeError("Can't initialize a PlatformSession without grant user and password")

        self._take_signon_control = signon_control if signon_control else True

        self._pending_stream_queue = []
        self._pending_data_queue = []

        self._refresh_grant = GrantRefreshToken()
        self._token_expiry_in_secs = 0
        self._refresh_token_thread = None
        self._websocket_endpoint = None

    def _init_streaming_config(self):
        # Set streaming configuration
        self._streaming_config.auth_token = self._access_token
        self._streaming_config.host = self._websocket_endpoint
        self._streaming_config.username = self._dacs_params.dacs_username
        self._streaming_config.position = self._dacs_params.dacs_position
        self._streaming_config.secure = True
        self._streaming_config.application_id = self._dacs_params.dacs_application_id
        self._streaming_config.login_message = {
            "Domain": "Login",
            "ID": 0,
            "Key": {
                "NameType": "AuthnToken",
                "Elements": {
                    "AuthenticationToken": self._access_token,
                    "ApplicationId": self._dacs_params.dacs_application_id,
                    "Position": self._dacs_params.dacs_position
                }
            }
        }

    #######################################
    #  methods to open and close session  #
    #######################################
    def open(self):
        if self._state in [Session.State.Pending, Session.State.Open]:
            # session is already opened or is opening
            return self._state

        # call Session.open() based on open_async() => _init_streaming_config will be called later
        return super(PlatformSession, self).open()

    def close(self):
        if self._refresh_token_thread:
            self._refresh_token_thread.cancel()
            self._refresh_token_thread.join()
        return super().close()

    ############################################
    #  methods to open asynchronously session  #
    ############################################
    async def open_async(self):
        if self._state in [Session.State.Pending, Session.State.Open]:
            # session is already opened or is opening
            return self._state

        # Go through the authentication process

        try:
            is_authorized = await self._authorize()
            if is_authorized:
                self._state = Session.State.Open
        except Exception as e:
            self.logger().warn(e, "EDP Authentication failed")
            # ReportSessionStatus(this, SessionStatus.AuthenticationFailed, DefineExceptionObj(e))
            self._state = Session.State.Closed
            self._status = Session.EventCode.SessionAuthenticationFailed

        if self._state is Session.State.Open:
            self.log(1, "Start to retrieve endpoint urls")
            try:
                await self._retrieve_streaming_endpoints()
                self._init_streaming_config()
            except Exception as e:
                self.logger().warn(e, "Streaming endpoint urls retrieving failed")
                # ReportSessionStatus(this, SessionStatus.AuthenticationFailed, DefineExceptionObj(e))

            await super(PlatformSession, self).open_async()
        return self._state

    ###############################################
    # Authentication Processing                   #
    ###############################################
    async def _authorize(self):
        # Authentication
        _grant = self._grant
        if isinstance(_grant, GrantPassword):
            self._refresh_grant.username(self._grant.get_username())
            _response = await self._request_access_token(_grant)
        elif isinstance(grant, GrantRefreshToken):
            _response = await self._request_refresh_token(_grant)
        else:
            raise ElektronError(-1, "Invalid EDP Authentication Grant specification")

        _authorized = self._check_token_response(_response)

        # Process the Refresh Token response
        if _authorized:
            # forward token to web socket
            self._init_refresh_token_thread()

        return _authorized

    async def _request_access_token(self, grant):
        if grant is None:
            raise ElektronError(-1, "AuthorizeUser is passed a null grant")

        _post_data = {
            "scope": grant.get_token_scope(),
            "grant_type": "password",
            "username": grant.get_username(),
            "password": grant.get_password(),
            "takeExclusiveSignOnControl": "true" if self._take_signon_control else "false"
        }
        if self.app_key is not None:
            _post_data["client_id"] = self.app_key

        self.log(logging.DEBUG, "Send request token to {}"
                 .format(PlatformSession.AuthEndpoint))
        self.log(1, "   \nwith post data {}\n   with auth {}"
                 .format(str(_post_data), grant.get_username()))

        try:
            _response = await self.http_request_async(method="POST",
                                                      url=PlatformSession.AuthEndpoint,
                                                      headers={"Accept": "application/json"},
                                                      data=_post_data,
                                                      auth=(grant.get_username(), ""))

            _response and self.log(1, "Request token response: {}".format(_response.text))
            return _response

        except Exception as e:
            self._status = Session.EventCode.StreamDisconnected
            raise ElektronError(-1, f"{e!r}")

    def _init_refresh_token_thread(self):
        # Give us 30 seconds leeway
        leeway = 30
        # Start our refresh token Timer
        _delay = int(self._token_expiry_in_secs) - leeway
        self._refresh_token_thread = PlatformSession.RefreshTokenThread(self, _delay)
        self._refresh_token_thread.daemon = True
        self._refresh_token_thread.start()

    def _check_token_response(self, response):
        if response is None:
            raise requests.exceptions.HTTPError("Response is None")

        if response.status_code != requests.codes.ok:
            # Looks like authentication failed.  Report an error
            self._status = Session.EventCode.SessionAuthenticationFailed
            self._last_event_code = Session.EventCode.SessionAuthenticationFailed
            try:
                _json = response.json()
                _error = _json.get("error")
                self._last_event_message = _json.get("error_description")
                self.log(logging.ERROR,
                         f"[Error {response.status_code} - {_error}] {self._last_event_message}")
            except ValueError:
                self._last_event_message = response.text
                self.log(logging.ERROR,
                         f"[Error {response.status_code} - {response.text}")

            self._on_event(self, self._last_event_code, self._last_event_message)
            return False

        self._status = Session.EventCode.SessionAuthenticationSuccess

        # Process the Authentication response
        _json_response = response.json()
        self._refresh_grant.refresh_token(_json_response["refresh_token"])
        self._access_token = _json_response["access_token"]
        self._token_expiry_in_secs = _json_response["expires_in"]
        return True

    ###############################################
    # Retrieve endpoints Processing               #
    ###############################################
    async def _retrieve_streaming_endpoints(self):
        """
        Send an HTTP request to retrieve the stream endpoints that can potentially
            be used by applications interested in stream data.

        :return: True (stream endpoints successfully retrieve), False (otherwise - error reported)
        """
        _request_data = {"transport": "websocket"}
        try:
            _response = await self.http_request_async(PlatformSession.StreamDiscoveryEndpoint,
                                                      method="GET", params=_request_data)
            self.log(logging.DEBUG, "Retrieve streaming endpoint response: {}".format(_response.text))
            if _response.status_code != requests.codes.ok:
                self._status = Session.EventCode.StreamDisconnected
                raise ElektronError(_response.status_code, _response.text)

            _json_response = _response.json()
            _services = _json_response["service"]
            self._ws_endpoints.clear()
            for _service in _services:
                if _service["transport"] == "websocket":
                    _endpoint = _service["endpoint"]
                    _port = _service["port"]
                    self._ws_endpoints.append(f"{_endpoint}:{_port}")

            if len(self._ws_endpoints) > 0:
                self._websocket_endpoint = self._ws_endpoints[0]

        except Exception as e:
            self._status = Session.EventCode.StreamDisconnected
            raise ElektronError(-1, f"{e!r}")

        return self._status

