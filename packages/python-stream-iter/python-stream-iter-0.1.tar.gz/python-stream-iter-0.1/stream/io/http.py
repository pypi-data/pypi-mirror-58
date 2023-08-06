import io as _io
import typing as _typing

import requests as _requests
from gimme_cached_property import cached_property

from stream.io import (
    BinaryFile as _BinaryFile,
)


class BaseHttpFile(_BinaryFile):
    def __init__(self, url: str):
        self.__url = url

    @property
    def url(self) -> str:
        return self.__url

    def __eq__(self, other):
        if not isinstance(other, BaseHttpFile):
            return False
        if self.url != other.url:
            return False
        return True

    # --- os ---

    @property
    def name(self) -> str:
        return self.url

    def fileno(self) -> int:
        raise self.NotSupported

    @property
    def isatty(self) -> bool:
        return False

    # --- seek ---

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        raise self.NotSupported

    def seek(self, offset: int, whence: int = _io.SEEK_SET) -> int:
        raise self.NotSupported

    def truncate(self, size: _typing.Optional[int] = None) -> int:
        raise self.NotSupported


class HttpDownloadFile(BaseHttpFile):
    def __init__(
            self,
            url: str,
            *,
            chuck_size: int = 8192,
    ):
        super().__init__(url)
        self.__chuck_size = chuck_size

        self.__request = _requests.get(self.url, stream=True)

    @property
    def _chuck_size(self) -> int:
        return self.__chuck_size

    @property
    def _request(self):
        return self.__request

    # --- os ---

    def __enter__(self):
        self.__request.__enter__()
        return self

    def close(self) -> None:
        self.__request.close()

    # --- read ---

    def readable(self) -> bool:
        return True

    @cached_property
    def _iter(self) -> _typing.Iterator[int]:
        for chunk in self._request.iter_content(chunk_size=self._chuck_size):
            if not chunk:
                continue  # filter out keep-alive new chunks
            yield from chunk

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
    parser.add_argument('url', type=str)
    parser.add_argument('file', type=str)
    args = parser.parse_args()

    with HttpDownloadFile(args.url) as f1:
        with LocalFile(args.file, 'wb') as f2:
            f1.copy_to(f2)


def get_cmd():
    import argparse
    from stream.io.std import StdOut, stderr
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()

    with HttpDownloadFile(args.url) as f:
        with StdOut() as stdout:
            try:
                f.copy_to(stdout.buffer)
            except BrokenPipeError:
                # avoid "exception ignored" message
                stderr.close()
