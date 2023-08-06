import typing as _typing

from stream import (
    Stream as _Stream,
)
from stream.typing import (
    T_co as _T_co,
)


class StreamStorage(_Stream[_T_co]):
    class Used(Exception):
        def __init__(self):
            super().__init__('Storage is used - do not store again.')

    class Empty(Exception):
        def __init__(self):
            super().__init__('Storage is empty.')

    def __init__(self):
        self.__iter = None

    def __bool__(self) -> bool:
        return self.__iter is not None

    def store(self, iterable: _typing.Iterable) -> None:
        """
        Usage:
                stream > storage.store
            or
                storage.store(iterable)
        """
        if self:
            raise self.Used
        self.__iter = iter(iterable)

    def __next__(self) -> _T_co:
        if not self:
            raise self.Empty
        return next(self.__iter)


class Streams(_typing.Mapping[_typing.Any, StreamStorage]):
    def __init__(self):
        self.__dict = {}

    def __contains__(self, k: _typing.Any) -> bool:
        return k in self.__dict

    def __getitem__(self, k: _typing.Any) -> StreamStorage:
        if k not in self:
            self.__dict[k] = StreamStorage()
        return self.__dict[k]

    def __len__(self) -> int:
        return len(self.__dict)

    def __iter__(self) -> _typing.Iterator[StreamStorage]:
        return iter(self.__dict)


class Node(object):
    """
    A node can take multiple input streams and generate multiple output streams accordingly.
    To use, please subclass and implement _connect().
    """
    __CONNECT_STATE_INITIAL = 1
    __CONNECT_STATE_STARTED = 2
    __CONNECT_STATE_FINISHED = 3
    __CONNECT_STATE_ERROR = 4

    class ConnectionError(Exception):
        def __init__(self, inner):
            super().__init__(
                'Connecting inputs with outputs has failed. '
                'Please only call `connect()` or `output` after all inputs are in place.'
            )
            self.inner = inner

    def __init__(self):
        self.__input = Streams()
        self.__output = Streams()

        self.__connect_state = self.__CONNECT_STATE_INITIAL
        self.__connect_error = None

    @property
    def input(self) -> Streams:
        return self.__input

    @property
    def output(self) -> Streams:
        self.connect()
        return self.__output

    def _connect(self):
        raise NotImplementedError  # pragma: no cover

    def __reset(self):
        self.__connect_state = self.__CONNECT_STATE_INITIAL
        self.__connect_error = None

    def __error(self, e):
        self.__connect_state = self.__CONNECT_STATE_ERROR
        self.__connect_error = e

    def __raise(self):
        if isinstance(self.__connect_error, NotImplementedError):
            raise self.__connect_error  # pragma: no cover
        else:
            raise self.ConnectionError(self.__connect_error)

    def connect(self, *, force_retry=False):
        if force_retry:
            self.__reset()

        if self.__connect_state == self.__CONNECT_STATE_ERROR:
            return self.__raise()
        elif self.__connect_state in (
                self.__CONNECT_STATE_STARTED,
                self.__CONNECT_STATE_FINISHED,
        ):
            return

        try:
            self.__connect_state = self.__CONNECT_STATE_STARTED
            self._connect()
        except Exception as e:
            self.__error(e)
            return self.__raise()
        else:
            self.__connect_state = self.__CONNECT_STATE_FINISHED
