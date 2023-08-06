import gzip as _gzip
import typing as _typing

from stream.io.iterable import (
    IterableFile as _BytesIO,
)
from .each import (
    ApplyEach as _ApplyEach,
)

encode: _ApplyEach[str, bytes] = _ApplyEach(str.encode, encoding='utf-8')
decode: _ApplyEach[bytes, str] = _ApplyEach(bytes.decode, encoding='utf-8')


def un_gzip(iterable: _typing.Iterable[bytes]) -> _typing.Iterator[bytes]:
    """
    Unzip a gzip byte stream, and split by lines.
    """
    readable = _BytesIO(iterable)
    with _gzip.open(readable, mode='rb') as f:
        yield from f
