import os as _os
import typing as _typing

from gimme_cached_property import cached_property

from . import (
    File as _File,
    BinaryFile as _BinaryFile,
    _wrapper,
)


class LocalFile(_wrapper.wrapper_class(open)):
    def __init__(
            self,
            path: str,
            mode: str = 'r',
            *args,
            **kwargs,
    ):
        """
        See params for `open`
        """
        super().__init__(path, mode, *args, **kwargs)
        self.__path = path
        self.__mode = mode

    @cached_property
    def path(self) -> str:
        return _os.path.realpath(self.__path)

    @property
    def text(self) -> bool:
        return 'b' not in self.__mode

    @cached_property
    def newline(self):
        if self.text:
            return '\n'
        else:
            return 10

    @cached_property
    def newline_str(self):
        if self.text:
            return '\n'
        else:
            return b'\n'

    def __eq__(self, other: _File):
        if not isinstance(other, LocalFile):
            return False
        if self.path != other.path:
            return False
        return True

    @cached_property
    def _buffer_class(self) -> _typing.Type[_BinaryFile]:
        if not self.text:
            raise AttributeError
        return _wrapper.buffer_class(self)

    @property
    def buffer(self) -> _BinaryFile:
        return self._buffer_class()
