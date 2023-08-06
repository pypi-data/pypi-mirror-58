import typing as _typing

from stream.mixins.each import (
    Each as _Each,
    ItemFunc as _ItemFunc,
)
from stream.mixins.match import (
    Match as _Match,
    BaseMatchFunc as _BaseMatchFunc,
    MatchFunc as _MatchFunc,
)
from stream.typing import (
    T_co as _T_co,
    V_co as _V_co,
)
from .each import (
    BaseOneToOneFunction as _BaseOneToOneFunction,
)


class BaseApplyIf(
    _BaseOneToOneFunction[_T_co, _V_co],
    _BaseMatchFunc[_T_co],
):
    def __call__(
            self,
            iterable: _typing.Iterable[_T_co],
    ) -> _typing.Iterator[_typing.Union[_T_co, _V_co]]:
        for item in iterable:
            if self.match(item):
                yield self.each(item)
            else:
                yield item


class ApplyIf(
    BaseApplyIf[_T_co, _V_co],
    _MatchFunc[_T_co],
    _ItemFunc[_T_co, _V_co],
):
    def __init__(
            self,
            match: _Match,
            each: _Each,
    ):
        _MatchFunc.__init__(self, match)
        _ItemFunc.__init__(self, each)
