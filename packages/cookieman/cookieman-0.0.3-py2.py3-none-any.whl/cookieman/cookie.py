"""Cookieman cookie classes."""

import functools

import six
import werkzeug.http
import werkzeug.datastructures
import flask
import flask.wrappers

import cookieman.exceptions as exceptions
import cookieman.limits as limits

try:
    import typing
    PartitionNameFunction = typing.Callable[[str, int], str]
except ImportError:
    pass


@functools.total_ordering
class Cookie(object):
    """Cookieman cookie."""

    header = 'Set-Cookie: '
    mapping_class = werkzeug.datastructures.ImmutableDict
    value_types = six.binary_type if six.PY2 else (six.binary_type, memoryview)
    dump_cookie_fnc = staticmethod(werkzeug.http.dump_cookie)
    byteview_fnc = staticmethod(memoryview.tobytes if six.PY2 else memoryview)

    @classmethod
    def default_partition_name_format(cls, name, index):
        # typing: (str, int) -> str
        """Get default partition name."""
        return '{}-{:x}'.format(name, index) if index else name

    @property
    def name(self):  # typing: () -> str
        """Get cookie name."""
        return self._name

    @property
    def value(self):  # typing: () -> str
        """Get cookie value."""
        return self._value

    @property
    def options(self):  # typing: () -> str
        """Get cookie options."""
        return self._options

    @property
    def data(self):  # type: () -> str
        """Get cookie header data."""
        if self._data is None:
            self._data = self.header + self.dump_cookie_fnc(
                self._name,
                self._value,
                max_size=0,
                **self._options
                )
        return self._data

    def __init__(self,
                 name,  # type: str
                 value=b'',  # type: bytes
                 options=None,  # type: typing.Optional[typing.Mapping]
                 ):  # type: (...) -> None
        """
        Initialize.

        :param name: cookie name
        :param value: cookie value
        :param options: cookie options
        """
        assert \
            isinstance(value, self.value_types), \
            TypeError('Cannot convert %r object to cookie' % type(value))
        self._data = None
        self._name = name
        self._value = value
        self._options = self.mapping_class(options or ())

    def __eq__(self, value):  # type: (Cookie) -> bool
        """Return self==value."""
        return self.data == value.data

    def __lt__(self, value):  # type: (Cookie) -> bool
        """Return self<value."""
        return (len(self.name), self.name) < (len(value.name), value.name)

    def __len__(self):  # type: () -> int
        """Return len(self)."""
        return len(self.data)

    def __repr__(self):  # type: () -> str
        """Return repr(self)."""
        return '<%s %r>' % (self.__class__.__name__, self.data)

    def partition(self,
                  maxsize,  # type: int
                  partition_name_fnc=None,  # type: PartitionNameFunction
                  ):  # type: (...) -> typing.Generator[Cookie, None, None]
        """
        Generate multiple cookies by spliting cookie value in chunks.

        :param maxsize: maximum total cookie size (including header)
        :param fmt_fnc: cookie name formatting
        :return: iterator of cookies
        """
        name_fnc = functools.partial(
            self.default_partition_name_format
            if partition_name_fnc is None else
            partition_name_fnc,
            self.name
            )
        byteview = self.byteview_fnc

        if len(self) < maxsize and name_fnc(0) == self.name:
            yield self
            return

        cls = self.__class__
        total = len(self.value)
        buffer = memoryview(self.value)
        bodysize = maxsize - len(cls('k', b'a', self.options)) + 2

        page = 0
        start = 0
        lastsize = 0

        while start < total or lastsize == maxsize:
            name = name_fnc(page)

            # retry on cookie excess due expansions
            for end in range(start + bodysize - len(name), start, -1):
                cookie = cls(name, byteview(buffer[start:end]), self.options)
                lastsize = len(cookie)

                if lastsize <= maxsize:
                    break
            else:
                raise exceptions.CookieSizeException(
                    'Unable to paginate cookies by size %d' % maxsize
                    )

            yield cookie
            start = end
            page += 1


class CookieProcessor(object):
    """Compressed-paginated and signed cookie manager."""

    cookie_class = Cookie

    def __init__(self,
                 session_interface,  # type: flask.sessions.SessionInterface
                 ):  # type: (...) -> None
        """
        Initialize.

        :param session_interface: flask session interface instance
        """
        self.session_interface = session_interface

    def get_cookie_options(self,
                           app,  # type: flask.Flask
                           browser,  # type: limits.Browser
                           ):  # type: (...) -> typing.Mapping[str, typing.Any]
        """
        Get cookie options dict as accepted by flask cookie dump methods.

        :param app: flask app
        :return: dict with options
        """
        return {
            'expires': self.session_interface.get_expiration_time(app),
            'path': self.session_interface.get_cookie_path(app),
            'domain': self.session_interface.get_cookie_domain(app),
            'secure': self.session_interface.get_cookie_secure(app),
            'httponly': self.session_interface.get_cookie_httponly(app),
            }

    def iter_request_cookies(self,
                             app,  # type: flask.Flask
                             request,  # type: flask.wrappers.Request
                             browser,  # type: limits.Browser
                             ):
        # type: (...) -> typing.Generator[cookie.Cookie, None, None]
        """
        Extract data from cookies.

        :param app: flask app
        :param request: flask request
        :param browser: cookieman browser limits
        :return: iterator of paginated cookies
        """
        cookies = request.cookies
        cookie_name = app.session_cookie_name
        cookie_prefix = '%s-' % app.session_cookie_name

        try:
            cookies = sorted(
                self.cookie_class(key, value.encode('ascii'))
                for key, value in request.cookies.items()
                if key == cookie_name or key.startswith(cookie_prefix)
                )
        except UnicodeEncodeError:
            cookies = ()

        if cookies:
            maxsize = len(cookies[0])
            for cookie in cookies:
                size = len(cookie)

                # spurious cookie
                if size > maxsize:
                    break

                yield cookie

                # paginated cookies have the same size except for the last one
                if size < maxsize:
                    break

    def iter_response_cookies(self,
                              app,  # type: flask.Flask
                              data,  # type: bytes
                              browser,  # type: limits.Browser
                              ):
        # (...) -> typing.Generator[cookie.Cookie, None, None]
        """
        Split given byte string for cookies.

        :param app: flask app
        :param data: byte string
        :param browser: cookieman browser limits
        :return: iterator of paginated cookie
        """
        options = self.get_cookie_options(app, browser)
        cookie = self.cookie_class(app.session_cookie_name, data, options)
        for page in cookie.partition(browser.maxsize):
            yield page
