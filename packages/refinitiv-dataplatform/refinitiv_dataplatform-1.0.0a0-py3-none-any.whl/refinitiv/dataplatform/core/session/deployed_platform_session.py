# coding: utf-8

__all__ = ["DeployedPlatformSession"]

from .session import Session


class DeployedPlatformSession(Session):

    class Params(Session.Params):
        def __init__(self, *args, **kwargs):
            super(DeployedPlatformSession.Params, self).__init__(*args, **kwargs)
            self._host = kwargs.get("host")

        def host(self, host):
            self._host = host
            return self

        def with_authentication_token(self, token):
            if token:
                self._dacs_params.authentication_token = token
            return self

    def __init__(self, app_key,
                 host=None,
                 authentication_token=None,
                 dacs_username=None,
                 dacs_position=None,
                 dacs_application_id=None,
                 on_state=None,
                 on_event=None, **kwargs):
        super().__init__(app_key=app_key,
                         token=authentication_token,
                         dacs_username=dacs_username,
                         dacs_position=dacs_position,
                         dacs_application_id=dacs_application_id,
                         on_state=on_state,
                         on_event=on_event)
        self._host = host

    def _init_streaming_config(self):
        self._streaming_config.host = self._host
        self._streaming_config.username = self._dacs_params.dacs_username
        self._streaming_config.application_id = self._dacs_params.dacs_application_id
        self._streaming_config.position = self._dacs_params.dacs_position
        self._streaming_config.login_message = {
            "ID": "",
            "Domain": "Login",
            "Key": {
                "Name": self._streaming_config.username,
                "Elements": {
                    "ApplicationId": self._streaming_config.application_id,
                    "Position": self._streaming_config.position
                }
            }
        }

    #######################################
    #  methods to open and close session  #
    #######################################
    def open(self):

        # call Session.open() based on open_async() => _init_streaming_config will be called later
        return super(DeployedPlatformSession, self).open()

    def close(self):
        return super(DeployedPlatformSession, self).close()

    ############################################
    #  methods to open asynchronously session  #
    ############################################
    async def open_async(self):
        self._init_streaming_config()

        await super(DeployedPlatformSession, self).open_async()
        await self.wait_for_streaming()

        if self._status == Session.EventCode.StreamConnected:
            self._state = Session.State.Open
        else:
            self._state = Session.State.Closed

        return self._state

