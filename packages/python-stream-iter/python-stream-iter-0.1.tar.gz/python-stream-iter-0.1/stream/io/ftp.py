import io as _io
import typing as _typing
from ftplib import (
    FTP as _FTP,
)
from io import (
    BytesIO as _BytesIO,
)
from queue import (
    Queue as _Queue,
)
from tempfile import (
    TemporaryFile as _TemporaryFile,
)
from threading import (
    Thread as _Thread,
)

from gimme_cached_property import cached_property

from . import (
    BinaryFile as _BinaryFile,
)
from .util import (
    characters as _characters,
)


class BaseFtpFile(_BinaryFile):
    class LoginStateError(Exception):
        pass

    @staticmethod
    def split_url(url: str) -> _typing.Tuple[str, str]:
        url = url.strip()
        if not url.startswith('ftp://'):
            raise ValueError
        host, path = url.split(':', maxsplit=1)[1].lstrip('/').split('/', maxsplit=1)
        return host, path

    def __init__(
            self,
            host: str,
            path: str,
            **kwargs,
    ):
        """
        :param host: ftp host
        :param path: file path on ftp server
        :param kwargs: See ftplib.FTP
        """
        self.__host = host
        self.__path = path
        self.__ftp: _FTP = None
        self.__kwargs = kwargs

    @property
    def host(self) -> str:
        return self.__host

    @property
    def path(self) -> str:
        return self.__path

    def _create_ftp(self) -> _FTP:
        return _FTP(self.host, **self.__kwargs)

    def login(self):
        if self.__ftp is not None:
            raise self.LoginStateError('Please do not login twice')
        self.__ftp = self._create_ftp()
        self.__ftp.login()

    def logout(self):
        if self.__ftp is None:
            raise self.LoginStateError('Please login before logging out')
        self.__ftp.close()
        self.__ftp = None

    @property
    def _ftp(self) -> _FTP:
        if self.__ftp is None:
            raise self.LoginStateError('Please login or use `with` context manager')
        return self.__ftp

    def __eq__(self, other):
        if not isinstance(other, BaseFtpFile):
            return False
        if self.host != other.host:
            return False
        if self.path != other.path:
            return False
        return True

    # --- os ---

    @property
    def name(self) -> str:
        return f"ftp://{self.host}/{self.path}"

    def fileno(self) -> int:
        raise self.NotSupported

    @property
    def isatty(self) -> bool:
        return False

    def __enter__(self) -> 'BaseFtpFile':
        self.login()
        return self

    def close(self) -> None:
        self.logout()

    # --- seek ---

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        raise self.NotSupported

    def seek(self, offset: int, whence: int = _io.SEEK_SET) -> int:
        raise self.NotSupported

    def truncate(self, size: _typing.Optional[int] = None) -> int:
        raise self.NotSupported


class FtpReadFile(BaseFtpFile):
    def __init__(
            self,
            host: str,
            path: str,
            *,
            threaded: bool = False,
            tmpfile: bool = False,
            blocksize: int = 8192,
            rest=None,
            **kwargs,
    ):
        """
        :param threaded:
            Use threading to iterate the downloading process.
            Default is False.
        :param tmpfile:
            Store downloaded data into a tmp file vs in memory.
            Default is False.
            Not available if `threaded` is True.

        :param blocksize: and
        :param rest:
            See FTP.retrbinary
        """
        super().__init__(host, path, **kwargs)
        self.__threaded = threaded
        self.__tmpfile = tmpfile
        self.__blocksize = blocksize
        self.__rest = rest

    @property
    def _threaded(self) -> bool:
        return self.__threaded

    @property
    def _tmpfile(self) -> bool:
        return self.__tmpfile

    @property
    def _blocksize(self) -> int:
        return self.__blocksize

    @property
    def _rest(self):
        return self.__rest

    @property
    def _ftp_cmd(self) -> str:
        return f"RETR {self.path}"

    def dump(self, callback: _typing.Callable[[bytes], _typing.Any]):
        self._ftp.retrbinary(
            self._ftp_cmd,
            callback,
            blocksize=self._blocksize,
            rest=self._rest,
        )

    def dump_to_buffer(self, buffer: _typing.BinaryIO):
        self.dump(buffer.write)

    # --- read ---

    def readable(self) -> bool:
        return True

    def _iter_threaded(self) -> _typing.Iterator[int]:
        ftp = self
        queue = _Queue(maxsize=1)

        class DownloadThread(_Thread):
            def run(self) -> None:
                ftp.dump(queue.put)

        thread = DownloadThread(daemon=True)
        thread.start()

        while True:
            if not thread.is_alive() and queue.empty():
                return
            data = queue.get()
            yield from data

    def _create_storage(self) -> _typing.BinaryIO:
        if self._tmpfile:
            return _TemporaryFile()
        else:
            return _BytesIO()

    @cached_property
    def _iter(self) -> _typing.Iterator[int]:
        if self._threaded:
            yield from self._iter_threaded()
            return

        with self._create_storage() as f:
            self.dump_to_buffer(f)
            f.seek(0, 0)
            yield from _characters(f)

    def _read_character(self) -> int:
        try:
            return next(self._iter)
        except StopIteration:
            raise self.EOF from None

    # --- not writable ---

    def writable(self) -> bool:
        return False

    def write(self, s: bytes) -> None:
        raise self.NotSupported

    def flush(self) -> None:
        raise self.NotSupported


def download_cmd():
    import argparse
    from stream.io.local import LocalFile
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, nargs='?')
    parser.add_argument('--host', '-H', type=str)
    parser.add_argument('--path', '-P', type=str)
    parser.add_argument('file', type=str)
    args = parser.parse_args()

    if args.url:
        host, path = FtpReadFile.split_url(args.url)
    else:
        host = args.host
        path = args.path

    with FtpReadFile(
            host,
            path,
    ) as f1:
        with LocalFile(args.file, 'wb') as f2:
            f1.dump_to_buffer(f2)


def get_cmd():
    import argparse
    from stream.io.std import StdOut, stderr
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, nargs='?')
    parser.add_argument('--host', '-H', type=str)
    parser.add_argument('--path', '-P', type=str)
    args = parser.parse_args()

    if args.url:
        host, path = FtpReadFile.split_url(args.url)
    else:
        host = args.host
        path = args.path

    with FtpReadFile(
            host,
            path,
    ) as f:
        with StdOut() as stdout:
            try:
                f.dump_to_buffer(stdout.buffer)
            except BrokenPipeError:
                # avoid "exception ignored" message
                stderr.close()
