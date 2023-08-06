import io as _io
import typing as _typing

from gimme_cached_property import cached_property

from stream import (
    Stream as _Stream,
    IterStream as _IterStream,
)

Character = _typing.TypeVar('Character', str, int)


class File(_typing.IO[_typing.AnyStr]):
    NotSupported = OSError
    EOF = EOFError

    @cached_property
    def stream(self) -> _Stream[_typing.AnyStr]:
        if not self.readable():
            raise self.NotSupported
        return _IterStream(self)

    @classmethod
    def stream_safe(cls, *args, **kwargs) -> _Stream[_typing.AnyStr]:
        def __iter() -> _typing.Iterator[_typing.AnyStr]:
            with cls(*args, **kwargs) as f:
                yield from f.stream

        return _IterStream(__iter())

    def input(self, lines: _typing.Iterable[_typing.AnyStr]) -> None:
        """
        Write a sequence of lines.
        Line endings are added.
        """
        for line in lines:
            self.write(line)
            self.write(self.newline_str)

    class SameFile(ValueError):
        pass

    def __eq__(self, other: 'File'):
        raise NotImplementedError  # pragma: no cover

    def copy_to(self, other: 'File'):
        if self == other:
            raise self.SameFile

        return self.stream > other.writelines

    # --- os ---

    @property
    def name(self) -> str:
        raise NotImplementedError  # pragma: no cover

    @property
    def mode(self) -> str:
        raise NotImplementedError  # pragma: no cover

    def fileno(self) -> int:
        raise NotImplementedError  # pragma: no cover

    @property
    def isatty(self) -> bool:
        raise NotImplementedError  # pragma: no cover

    def close(self) -> None:
        raise NotImplementedError  # pragma: no cover

    @property
    def closed(self) -> bool:
        raise NotImplementedError  # pragma: no cover

    class Closed(ValueError):
        pass

    def __enter__(self) -> 'File':
        if self.closed:
            raise self.Closed
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    # --- seek ---

    def seekable(self) -> bool:
        raise NotImplementedError  # pragma: no cover

    def tell(self) -> int:
        raise NotImplementedError  # pragma: no cover

    def seek(self, offset: int, whence: int = _io.SEEK_SET) -> int:
        raise NotImplementedError  # pragma: no cover

    def truncate(self, size: _typing.Optional[int] = None) -> int:
        raise NotImplementedError  # pragma: no cover

    def _move_next_pos(self) -> None:
        """
        Used by reading one character.
        """
        pass

    # --- read ---

    def readable(self) -> bool:
        raise NotImplementedError  # pragma: no cover

    def _read_character(self) -> Character:
        """
        Subclasses:

        Raise OSError (self.NotSupported) for non-readable files;
        Return single character (str or bytes);
        Raise EOFError (self.EOF) if finished.
        """
        raise NotImplementedError  # pragma: no cover

    @property
    def newline(self) -> Character:
        raise NotImplementedError  # pragma: no cover

    @property
    def newline_str(self) -> _typing.AnyStr:
        raise NotImplementedError  # pragma: no cover

    def _read_iter(
            self,
            *,
            n: int = None,
            line: bool = False,
    ) -> _typing.Iterator[Character]:
        i = 0
        while True:
            if n is not None and i >= n:
                return
            try:
                b = self._read_character()
            except self.EOF:
                return
            yield b
            i += 1
            self._move_next_pos()
            if line and b == self.newline:
                return

    def _read(
            self,
            *,
            n: int = None,
            line: bool = False,
    ) -> _typing.AnyStr:
        """
        Subclasses:

        Use _read_iter to generate result.
        Differs for str and bytes.
        """
        raise NotImplementedError  # pragma: no cover

    def read(self, n: int = -1) -> _typing.AnyStr:
        if n == -1:
            n = None
        return self._read(n=n, line=False)

    def readline(self, limit: int = -1) -> _typing.AnyStr:
        if limit == -1:
            limit = None
        return self._read(n=limit, line=True)

    def _readlines(
            self,
            *,
            n: int = None,
    ) -> _typing.Iterator[_typing.AnyStr]:
        i = 0
        while True:
            if n is not None and i >= n:
                return
            line = self.readline()
            if not line:
                return
            yield line
            i += 1

    def readlines(self, hint: int = -1) -> _typing.List[_typing.AnyStr]:
        if hint == -1:
            hint = None
        return list(self._readlines(n=hint))

    def __next__(self) -> _typing.AnyStr:
        return next(self._readlines(n=1))

    def __iter__(self) -> _typing.Iterator[_typing.AnyStr]:
        return self._readlines()

    # --- write ---

    def writable(self) -> bool:
        raise NotImplementedError  # pragma: no cover

    def write(self, s: _typing.AnyStr) -> None:
        """
        Subclasses:

        Raise OSError (self.NotSupported) for non-readable files.
        """
        raise NotImplementedError  # pragma: no cover

    def writelines(self, lines: _typing.Iterable[_typing.AnyStr]) -> None:
        """
        Write a sequence of lines.
        Note: line separators are not added
        """
        for line in lines:
            self.write(line)

    def flush(self) -> None:
        raise NotImplementedError  # pragma: no cover


class TextFile(File[str], _typing.TextIO):
    @property
    def newline(self) -> str:
        return '\n'

    @property
    def newline_str(self) -> str:
        return '\n'

    def _read(
            self,
            *,
            n: int = None,
            line: bool = False,
    ) -> str:
        return ''.join(self._read_iter(n=n, line=line))

    # --- text io ---

    @property
    def buffer(self) -> 'BinaryFile':
        raise NotImplementedError  # pragma: no cover

    @property
    def encoding(self) -> str:
        raise NotImplementedError  # pragma: no cover

    @property
    def errors(self) -> _typing.Optional[str]:
        raise NotImplementedError  # pragma: no cover

    @property
    def line_buffering(self) -> int:
        raise NotImplementedError  # pragma: no cover

    @property
    def newlines(self) -> _typing.Union[str, _typing.Tuple[str, ...], None]:
        raise NotImplementedError  # pragma: no cover


class BinaryFile(File[bytes], _typing.BinaryIO):
    @property
    def newline(self) -> int:
        return 10  # b'\n'

    @property
    def newline_str(self) -> bytes:
        return b'\n'

    def _read(
            self,
            *,
            n: int = None,
            line: bool = False,
    ) -> bytes:
        return bytes(self._read_iter(n=n, line=line))
