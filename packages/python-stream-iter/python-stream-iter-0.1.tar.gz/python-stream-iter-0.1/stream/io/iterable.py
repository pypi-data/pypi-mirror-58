import io as _io
import typing as _typing

from stream.functions.collections import (
    yield_from as _yield_from,
)
from . import (
    BinaryFile as _BinaryFile,
)


class IterableFile(_BinaryFile):
    def __init__(self, iterable: _typing.Iterable[bytes]):
        self.__iter = _yield_from(iterable)
        self.__pointer = 0

    def __eq__(self, other):
        return False

    # --- os ---

    @property
    def name(self) -> str:
        return str(self)

    @property
    def mode(self) -> str:
        return 'rb'

    def fileno(self) -> int:
        raise self.NotSupported

    def isatty(self) -> bool:
        return False

    def close(self) -> None:
        pass

    @property
    def closed(self) -> bool:
        return False

    # --- seek ---

    def seekable(self) -> bool:
        return True

    def tell(self) -> int:
        return self.__pointer

    def seek(self, offset: int, whence: int = _io.SEEK_SET) -> int:
        if whence == _io.SEEK_END:
            raise self.NotSupported
        if whence == _io.SEEK_SET:
            if offset < self.__pointer:
                raise self.NotSupported
            offset = self.__pointer + offset
        if offset < 0:
            raise self.NotSupported
        self._read(n=offset)
        return self.__pointer

    def truncate(self, size: int = None) -> int:
        raise self.NotSupported

    def _move_next_pos(self) -> None:
        self.__pointer += 1

    # --- read ---

    def readable(self) -> bool:
        return True

    def _read_character(self) -> int:
        try:
            return next(self.__iter)
        except StopIteration:
            raise self.EOF from None

    # --- not writable ---

    def writable(self) -> bool:
        return False

    def write(self, s: bytes) -> None:
        raise self.NotSupported

    def flush(self) -> None:
        raise self.NotSupported
