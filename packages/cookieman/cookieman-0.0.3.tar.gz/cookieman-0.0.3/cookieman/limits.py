"""Cookieman browser limits and shrinking classes."""

import io
import sys
import itertools
import functools
import collections

import six
import six.moves
import werkzeug.datastructures

import cookieman.resources as resources
import cookieman.exceptions as exceptions

try:
    import typing
    TCookie = typing.TypeVar('TCookie', bound=typing.Sized)
    LimitsSection = typing.Tuple[str, typing.Mapping[str, str]]
    ShrinkFunction = typing.Callable[
        [typing.MutableMapping, bool],
        typing.MutableMapping
        ]
    ShrinkFunctionGenerator = typing.Generator[
        typing.Callable[
            [typing.MutableMapping],
            typing.MutableMapping
            ],
        typing.Tuple[typing.Iterable[str], bool],
        None
        ]
except ImportError:
    pass


class Browser(object):
    """
    Browser limits.

    :attr name: browser name
    :type name: str
    :attr platform: browser platform (generic OS name)
    :type platform: str
    :attr version: browser name
    :type version: Tuple[Union[int, str]]
    :attr maxcookies: maximum supported number of cookies
    :type maxcookies: int
    :attr maxsize: maximum supported size of a single cookie
    :type maxsize: int
    :attr maxtotal: maximum total supported size of all cookies
    :type maxtotal: int
    """

    __slots__ = (
        'name', 'platform', 'version', 'maxcookies', 'maxsize',
        'maxtotal',
        )

    def __init__(self,
                 name='',  # type: str
                 platform='',  # type: str
                 version=(),  # type: typing.Iterable[str]
                 maxcookies=1,  # type: int
                 maxsize=4096,  # type: int
                 maxtotal=None,  # type: typing.Optional[int]
                 ):  # type: (...) -> None
        """
        Initialize.

        :param name: browser name
        :param platform: browser platform
        :param version: browser version
        :param maxcookies: maximum number of cookies
        :param maxsize: maximum number of bytes of every cookies
        :param maxtotal: maximum number of total bytes of all cookies
        """
        self.name = name
        self.platform = platform
        self.version = tuple(version)
        self.maxcookies = maxcookies
        self.maxsize = maxsize
        self.maxtotal = (
            min(maxtotal, maxcookies * maxsize)
            if maxcookies and maxtotal else
            maxtotal
            if maxtotal else
            maxcookies * maxsize
            )

    def __repr__(self):  # type: () -> str
        """
        Return repr(self).

        :return: string representation of object
        """
        name = '%s.%s' % (
            self.__class__.__module__,
            self.__class__.__name__
            )
        props = {attr: getattr(self, attr) for attr in self.__slots__}
        return '<%s%r>' % (name, props)

    @classmethod
    def parse_version(cls,
                      version,  # type:  typing.Iterable[str]
                      ):
        # type: (...) -> typing.Iterable[typing.Union[int, str]]
        """
        Convert version (str or tuple) to version tuple.

        :param version: version value (str or tuple)
        :type version:
        :return: version tuple
        """
        string_types = six.string_types
        if version:
            if isinstance(version, string_types):
                version = version.split('.')
            return tuple(
                int(i) if isinstance(i, string_types) and i.isdigit() else i
                for i in version
                )
        return ()

    @classmethod
    def from_spec(cls,
                  name,  # type: str
                  properties,  # type: typing.Mapping[str, str]
                  ):  # type: (...) -> Browser
        """
        Create browser object based on limits database data.

        :param name: browser identifier (name:platform:version)
        :param properties:
        :returns: browser object
        """
        name, platform, version = name.split(':')[:3]
        return cls(
            name,
            platform or '',
            cls.parse_version(version),
            int(properties['maxcookies']),
            int(properties['maxsize']),
            int(properties['maxtotal']),
            )


class Limits(object):
    """Browser limits database."""

    browser_class = Browser
    mapping_class = werkzeug.datastructures.ImmutableDict

    def __init__(self,
                 browsers=(),  # type: typing.Iterable[Browser]
                 ):  # type: (...) -> None
        """
        Initialize.

        :param browsers: iterable with all available browsers
        """
        self.browsers_by_key = self.mapping_class(
            (key, tuple(browsers)) for key, browsers in itertools.groupby(
                sorted(
                    browsers,
                    key=lambda browser: (browser.name, browser.platform,
                                         browser.version),
                    reverse=True,
                ),
                key=lambda browser: (browser.name, browser.platform)))
        self.default = self.browser_class()

    def get(self,
            name='',  # type: str
            platform='',  # type: str
            version=(),  # type: typing.Iterable[str]
            ):  # type: (...) -> Browser
        """
        Get browser limits object matching giving criteria.

        :param name: browser name
        :param platform: browser platform name
        :param version: browser version tuple
        :return: browser limits object
        """
        version = self.browser_class.parse_version(version)
        search_keys = (
            ((name, platform), version),
            ((name, platform), ()),
            ((name, ''), version),
            ((name, ''), ()),
            (('', ''), ()),  # database default
            )
        for (key, version) in search_keys:
            for browser in self.browsers_by_key.get(key, ()):
                if browser.version <= version:
                    return browser
        return self.default

    def __eq__(self, value):  # type: (Limits) -> bool
        """Return self==value."""
        return (
            isinstance(value, self.__class__) and
            self.browsers_by_key == value.browsers_by_key
            )

    if six.PY2:
        @classmethod
        def get_sections(cls, data):
            # type: (str) -> typing.Generator[LimitsSection, None, None]
            """Yield sections from config data."""
            parser = six.moves.configparser.SafeConfigParser()
            with io.StringIO(data) as f:
                parser.readfp(f)
                for name in parser.sections():
                    yield name, dict(parser.items(name))
    else:
        @classmethod
        def get_sections(cls, data):
            # type: (str) -> typing.Generator[LimitsSection, None, None]
            """Yield sections from config data."""
            parser = six.moves.configparser.ConfigParser()
            parser.read_string(data)

            for name in parser.sections():
                yield name, parser[name]

    @classmethod
    def load(cls, path=None):  # type: (typing.Optional[str]) -> Limits
        """
        Load browser limits database file.

        If no path is given, cookieman builtin limits database will be used.

        :param path: path or None
        :returns: Limits object
        """
        if path is None:
            data = resources.read_text('limits.ini')
        else:
            with open(path, 'rb') as f:
                data = f.read().decode('utf-8')

        return cls(
            cls.browser_class.from_spec(name, value)
            for name, value in cls.get_sections(data)
            )


class ShrinkManager(object):
    """Cookie shrinking function manager."""

    _key_added_exc = type('KeyAdded', (Exception, ), {})

    def __init__(self):
        """Initialize."""
        self.handlers = collections.defaultdict(set)

    if typing:
        @typing.overload
        def register(self,
                     key_or_keys,  # type: typing.Iterable[str]
                     shrink_fnc=None,  # type: typing.Literal[None]
                     ):
            # type: (...) -> typing.Callable[[ShrinkFunction], ShrinkFunction]
            """Define register typing overload. Implemented below."""

        @typing.overload
        def register(self,
                     key_or_keys,  # type: typing.Iterable[str]
                     shrink_fnc,  # type: ShrinkFunction
                     ):
            # type: (...) -> ShrinkFunction
            """Define register typing overload. Implemented below."""

    def register(self, key_or_keys, shrink_fnc=None):
        """
        Register a session shrinking function for given keys.

        This method can be used as decorator.

        :param key_or_keys: key or list of keys would be affected
        :param shrink_fnc: shrinking function (optional for decorator)
        :returns: either original given shrink_fnc or decorator

        Usage:

        .. code-block:: python

            @shrinker.register('my_session_key')
            def my_shrink_fnc(data):
                del data['my_session_key']
                return data

        """
        if shrink_fnc is None:
            return functools.partial(self.register, key_or_keys)

        keys = (
            (key_or_keys,)
            if isinstance(key_or_keys, six.string_types) else
            key_or_keys
            )
        for name in keys:
            self.handlers[name].add(shrink_fnc)
        return shrink_fnc

    @classmethod
    def _purge(cls,
               key,  # type: str
               data,  # type: typing.MutableMapping
               last,  # type: bool
               ):  # type: (...) -> typing.MutableMapping
        """
        Remove an unhandled key.

        :param key: data dict key to remove
        :param data: data mapping
        :param last: ignored
        :returns: updated mapping
        """
        del data[key]
        return data

    def _iter_handled(self, keys, last=False):
        # type: (typing.Iterable[str], bool) -> ShrinkFunctionGenerator
        """
        Iterate shrinking functions with fixed second (last) parameter.

        :param keys:
        :param last:
        :returns: generator of callables
        """
        again = True
        handlers = self.handlers
        visited = set()
        while again:
            again = False
            for key in tuple(keys):
                if key in visited:
                    continue

                revisit = False
                for handler in handlers.get(key, ()):
                    if key not in keys:
                        revisit = False
                        break

                    keys, shrunk = (yield lambda data: handler(data, last))
                    revisit |= shrunk

                if revisit:
                    again = True
                else:
                    visited.add(key)

    def _iter_purge(self, keys, last=False):
        # type: (typing.Iterable[str], bool) -> ShrinkFunctionGenerator
        """
        Iterate purge functions with fixed key and last parameters.

        :param keys:
        :param last:
        :return: generator of callables
        """
        handlers = self.handlers
        for key in tuple(keys):
            if last or key not in handlers:
                yield (lambda data: self._purge(key, data, last))

    def _iter_tasks(self, keys):
        # type: (typing.Iterable[str]) -> ShrinkFunctionGenerator
        """
        Iterate functions from different shrinking strategies.

        Generators emits functions accepting the mapping and receiving
        both data and wether data size changes.

        :param keys: possible handler keys to iterate
        :return: generator of callables

        Iteration order:

        1. Shrinking functions for keys on data.
        2. Purging functions for unhandled keys.
        3. Shrinking functions for keys on data (receiving last=True)
        4. Purging functions for every key.

        """
        strategies = [
            lambda keys: self._iter_handled(keys),
            lambda keys: self._iter_purge(keys),
            lambda keys: self._iter_handled(keys, True),
            lambda keys: self._iter_purge(keys, True),
            ]
        for strategy in strategies:
            strategy_iter = strategy(keys)
            try:
                keys, changed = (yield next(strategy_iter))
                while True:
                    keys, changed = (yield strategy_iter.send((keys, changed)))
            except StopIteration:
                pass

    def shrink(self,
               data,  # type: typing.MutableMapping
               browser,  # type: Browser
               dump_fnc,  # type: typing.Callable[[typing.Any], bytes]
               serialize_fnc,  # type: typing.Callable[[bytes], TCookie]
               ):  # type: (...) -> typing.Iterable[TCookie]
        """
        Apply shrink functions to data until under browser limits.

        If it's not possible, raises error.

        :param data: mapping
        :param browser: browser limits object
        :param dump_fnc: callable which returns binary data payload
        :param serialize_fnc: callable which returns cookies
        :return: multiple paginates cookies
        :raises exceptions.CookieSizeException: if unable to shrink enough
        """
        handlers_iter = None
        old_size = sys.maxsize
        maxsize = browser.maxsize
        maxcookies = browser.maxcookies

        while True:
            payload = dump_fnc(data)
            cookies = list(serialize_fnc(payload))
            size = sum(map(len, cookies))

            if size <= maxsize and len(cookies) <= maxcookies:
                return cookies

            try:
                if handlers_iter:
                    shrunk = len(payload) < old_size
                    handler = handlers_iter.send((data, shrunk))
                else:
                    handlers_iter = iter(self._iter_tasks(data))
                    handler = next(handlers_iter)
            except StopIteration:
                break

            old_size = len(payload)
            data = handler(data)

        raise exceptions.CookieSizeException(
            'Session cookies exceeded browser maxsize %d' % (
                browser.maxsize,
                )
            if len(cookies) > maxsize else
            'Session cookies exceeded browser maxcookies %d' % (
                browser.maxcookies
                )
            )
