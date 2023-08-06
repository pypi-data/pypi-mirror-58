"""Cookieman flask-compatible session module."""

import six.moves
import flask.wrappers
import flask.sessions
import werkzeug.datastructures

try:
    import typing
except ImportError:
    pass


class LazySession(six.moves.UserDict, flask.sessions.SessionMixin):
    """Session mapping with deferred data loading."""

    callback_dict_class = werkzeug.datastructures.CallbackDict

    modified = False
    accessed = False

    def _notify_update(self, data):  # type: (typing.Any) -> None
        """
        Flag this object as modified.

        Used as werkzeug CallbackDict callback.

        :param data: ignored
        """
        self.modified = True
        self.accessed = True

    def __init__(self,
                 session_data_fnc,  # type: typing.Callable[[], dict]
                 request=None,  # type: typing.Optional[flask.wrappers.Request]
                 ):  # type: (...) -> None
        """
        Initialize.

        :param session_data_fnc: session data getter function
        :param request: request object
        """
        self._data = None
        self._session_data_fnc = session_data_fnc
        self._request = request

    @property
    def data(self):  # type: () -> typing.Mapping
        """
        Return session data mapping.

        :return: inner session mapping object
        """
        self.accessed = True
        if self._data is None:
            self._data = self.callback_dict_class(
                self._session_data_fnc(),
                self._notify_update,
                )
        return self._data

    # TODO (on python2 drop): remove
    def __iter__(self):  # type: () -> typing.Iterator[typing.Any]
        """
        Return iter(x).

        :return: keys in session mapping
        """
        return iter(self.data)
