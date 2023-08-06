import typing as _typing

from stream.mixins.match import (
    BaseMatchFunc as _BaseMatchFunc,
    MatchFunc as _MatchFunc,
)
from stream.typing import (
    Function as _Function,
    T_co as _T_co,
)
from stream.util.func.partial import (
    PartialFunc as _PartialFunc,
)


class BaseFilter(
    _Function[_T_co, _T_co],
    _BaseMatchFunc[_T_co],
):
    def __call__(self, iterable: _typing.Iterable[_T_co]) -> _typing.Iterator[_T_co]:
        for item in iterable:
            if not self.match(item):
                continue
            yield item

    def __invert__(self):
        return Filter(~self.match_f)

    def __and__(self, other: 'BaseFilter'):
        return Filter(self.match_f & other.match_f)

    def __or__(self, other: 'BaseFilter'):
        return Filter(self.match_f | other.match_f)


class Filter(
    BaseFilter[_T_co],
    _MatchFunc[_T_co],
):
    """
    Check all items in the iterable, and yield only matches.
    """

    def __init__(self, match, *args, **kwargs):
        match = _PartialFunc(match, *args, **kwargs)
        _MatchFunc.__init__(self, match)


remove_empty = Filter(bool)
