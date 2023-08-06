import typing as _typing

from .each import (
    ApplyEach as _ApplyEach,
)
from .filter import (
    Filter as _Filter,
)

strip: _ApplyEach[str, str] = _ApplyEach(str.strip)

remove_comments: _Filter[str] = ~_Filter(str.startswith, '#')


def split_lines(iterable: _typing.Iterable[str]) -> _typing.Iterator[str]:
    """
    :param iterable: a series of strings, not necessarily split by lines
    :return: a series of strings split by lines

    E.g.
        ('123', '45\n6\n') | split_lines -> ('12345\n', '6\n')
    """
    remaining = ''
    for item in iterable:
        lines = (remaining + item).splitlines(keepends=True)
        remaining = lines.pop(-1)
        yield from lines
    if remaining:
        yield remaining
