# coding: utf8

from refinitiv.dataplatform.core.session import Session, DesktopSession, DeployedPlatformSession, PlatformSession, GrantPassword

__all__ = ['CoreFactory',
           'open_deployed_platform_session',
           'open_desktop_session',
           'open_platform_session'
           #'close_session'
           ]


class CoreFactory:

    @staticmethod
    def create_session(session_params):
        if isinstance(session_params, Session.Params):
            # check the platform
            if isinstance(session_params, DesktopSession.Params):
                return DesktopSession(app_key=session_params._app_key,
                                      on_state=session_params._on_state_cb,
                                      on_event=session_params._on_event_cb,
                                      token=session_params._dacs_params.authentication_token,
                                      dacs_username=session_params._dacs_params.dacs_username,
                                      dacs_position=session_params._dacs_params.dacs_position,
                                      dacs_application_id=session_params._dacs_params.dacs_application_id)
            elif isinstance(session_params, DeployedPlatformSession.Params):
                return DeployedPlatformSession(app_key=session_params._app_key,
                                               host=session_params._host,
                                               on_state=session_params._on_state_cb,
                                               on_event=session_params._on_event_cb,
                                               token=session_params._dacs_params.authentication_token,
                                               dacs_username=session_params._dacs_params.dacs_username,
                                               dacs_position=session_params._dacs_params.dacs_position,
                                               dacs_application_id=session_params._dacs_params.dacs_application_id)
            elif isinstance(session_params, PlatformSession.Params):
                return PlatformSession(app_key=session_params._app_key,
                                       grant=session_params.get_grant(),
                                       signon_control=session_params.take_signon_control(),
                                       on_state=session_params._on_state_cb,
                                       on_event=session_params._on_event_cb,
                                       token=session_params._dacs_params.authentication_token,
                                       dacs_username=session_params._dacs_params.dacs_username,
                                       dacs_position=session_params._dacs_params.dacs_position,
                                       dacs_application_id=session_params._dacs_params.dacs_application_id)
        else:
            raise Exception("Wrong session parameter")

    @staticmethod
    def create_desktop_session(app_key, on_state=None, on_event=None):
        return DesktopSession(app_key, on_state, on_event)

    @staticmethod
    def create_platform_session(app_key,
                                oauth_grant_type,
                                take_signon_control=True,
                                dacs_username=None,
                                dacs_position=None,
                                dacs_application_id=None,
                                on_state=None,
                                on_event=None):
        return PlatformSession(app_key=app_key,
                               grant=oauth_grant_type,
                               signon_control=take_signon_control,
                               dacs_username=dacs_username,
                               dacs_application_id=dacs_application_id,
                               dacs_position=dacs_position,
                               on_state=on_state,
                               on_event=on_event)

    @staticmethod
    def create_deployed_platform_session(app_key,
                                         host,
                                         authentication_token=None,
                                         dacs_username=None,
                                         dacs_position=None,
                                         dacs_application_id=None,
                                         on_state=None,
                                         on_event=None):
        return DeployedPlatformSession(app_key=app_key,
                                       host=host,
                                       authentication_token=authentication_token,
                                       dacs_username=dacs_username,
                                       dacs_application_id=dacs_application_id,
                                       dacs_position=dacs_position,
                                       on_state=on_state,
                                       on_event=on_event)


def open_desktop_session(app_key):
    from refinitiv.dataplatform.function.tools import set_default_session
    session = CoreFactory.create_desktop_session(app_key)
    close_session()
    set_default_session(session)
    session.open()
    return session


def open_platform_session(app_key, grant):
    from refinitiv.dataplatform.function.tools import set_default_session
    session = CoreFactory.create_platform_session(app_key, grant)
    close_session()
    set_default_session(session)
    session.open()
    return session


def open_deployed_platform_session(app_key,
                                   deployed_platform_host,
                                   deployed_platform_username):
    from refinitiv.dataplatform.function.tools import set_default_session
    session = CoreFactory.create_deployed_platform_session(app_key,
                                                           deployed_platform_host,
                                                           deployed_platform_username)
    close_session()
    set_default_session(session)
    session.open()
    return session


def close_session():
    from refinitiv.dataplatform.function.tools import DefaultSession
    DefaultSession.close_default_session()
