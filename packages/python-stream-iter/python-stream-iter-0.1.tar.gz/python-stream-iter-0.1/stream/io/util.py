import typing as _typing

from . import (
    Character as _Character,
)


def characters(file: _typing.IO) -> _typing.Iterator[_Character]:
    while True:
        char = file.read(1)
        if not char:
            return
        yield char
