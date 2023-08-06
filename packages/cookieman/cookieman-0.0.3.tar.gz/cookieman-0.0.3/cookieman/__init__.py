"""Cookieman compressed, paginated and signed session cookies."""

__version__ = '0.0.3'

import datetime

try:
    import typing
except ImportError:
    pass

import flask
import flask.wrappers
import flask.sessions
import flask.helpers

import cookieman.cookie as cookie
import cookieman.serializer as serializer
import cookieman.session as session
import cookieman.limits as limits


class CookieMan(flask.sessions.SessionInterface):
    """Compressed, paginated and signed session cookie manager."""

    limits_class = limits.Limits
    shrink_class = limits.ShrinkManager
    cookie_processor_class = cookie.CookieProcessor
    serializer_class = serializer.CookieManSerializer
    session_class = session.LazySession

    def __init__(self, salt='session-cookie'):  # type: (str) -> None
        """
        Initialize.

        :param salt: cookie signature salt
        """
        self._cookie_processor = self.cookie_processor_class(self)
        self._cookie_shrink = self.shrink_class()
        self._limits_cache = {}
        self.salt = salt

    def register(self,
                 key_or_keys,  # type: typing.Union[str, typing.Iterable[str]]
                 shrink_fnc=None,  # type: limits.ShrinkFunction
                 ):  # type: (...) -> limits.ShrinkFunction
        """
        Register a session shrinking function for given keys.

        This method can be used as decorator.

        :param key_or_keys: key or iterable of keys would be affected
        :param shrink_fnc: shrinking function (optional for decorator)
        :returns: either original given shrink_fnc or decorator

        Usage:

        .. code-block:: python

            @app.session_interface.register('my_session_key')
            def my_shrink_fnc(data):
                del data['my_session_key']
                return data

        """
        return self._cookie_shrink.register(key_or_keys, shrink_fnc)

    def get_browser(self,
                    app,  # type: flask.Flask
                    request,  # type: flask.wrappers.Request
                    ):  # type: (...) -> limits.Browser
        """
        Get browser limits object based on app and request.

        :param app: flask app object
        :returns: limits object
        """
        limits_file = app.config.get('COOKIEMAN_LIMITS_PATH', None)
        if limits_file not in self._limits_cache:
            self._limits_cache[limits_file] = \
                self.limits_class.load(limits_file)
        return self._limits_cache[limits_file].get(
            request.user_agent.browser,
            request.user_agent.platform,
            request.user_agent.version,
            )

    def get_signing_serializer(self,
                               app,  # type: flask.Flask
                               ):
        # type: (...) -> typing.Optional[serializer.CookieManSerializer]
        """
        Get signing serializer class instance for given app.

        :param app: application instance
        :returns: instance if app has secret key else None
        :rtype: None or serializer class
        """
        if not app.secret_key:
            return None
        return self.serializer_class(app.secret_key, self.salt)

    def get_expiration_time(self,
                            app,  # type: flask.Flask
                            session=None,  # type: typing.Any
                            ):  # type: (...) -> datetime.datetime
        """
        Get expiration time for a new cookie based on app config.

        :param app: flask app
        :param session: ignored
        ;returns: expiration time
        """
        return datetime.datetime.utcnow() + app.permanent_session_lifetime

    def open_session(self,
                     app,  # type: flask.Flask
                     request,  # type: flask.wrappers.Request
                     ):  # type: (...) -> typing.Optional[session.LazySession]
        """
        Create lazy session from request cookies.

        :param app: flask app object
        :param request: request object to extract
        :returns: session dict-like object
        """
        def extract_cookie_data():
            data = b''.join(
                cookie.value
                for cookie in self._cookie_processor.iter_request_cookies(
                    app,
                    request,
                    self.get_browser(app, request),
                    )
                )
            if data:
                max_age = flask.helpers.total_seconds(
                    app.permanent_session_lifetime
                    )
                try:
                    return serializer.loads(data, max_age=max_age)
                except Exception:
                    pass
            return {}

        serializer = self.get_signing_serializer(app)
        if serializer:
            return self.session_class(extract_cookie_data, request)
        return None

    def save_session(self,
                     app,  # type: flask.Flask
                     session,  # type: session.LazySession
                     response,  # type: flask.wrappers.Response
                     ):  # type: (...) -> None
        """
        Update response in-place with session cookies.

        :param app: flask app object
        :param session: cookieman session object
        :param response: flask response object
        :returns: given response object (with cookie changes)
        """
        request = getattr(session, '_request', None) or flask.request
        browser = self.get_browser(app, request)
        cookies = self._cookie_processor

        if session.modified and not session:
            options = cookies.get_cookie_options(app, browser)
            response.delete_cookie(
                app.session_cookie_name,
                domain=options['domain'],
                path=options['path'],
                )
            return

        if session.accessed and session:
            response.vary.add('Cookie')

        if not self.should_set_cookie(app, session):
            return

        iter_cookies = cookies.iter_response_cookies
        cookies = self._cookie_shrink.shrink(
            dict(session),
            browser,
            self.get_signing_serializer(app).dumps,
            lambda payload: iter_cookies(app, payload, browser)
            )

        for c in cookies:
            response.set_cookie(c.name, c.value, **c.options)
