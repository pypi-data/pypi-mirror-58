import typing as _typing

from gimme_cached_property import cached_property
from logical import (
    BaseFunction as _BaseLogicalFunction,
)
from logical.boolean import (
    false as _false,
)
from logical.comparison import (
    LessThan as _Lt,
    GreaterThanOrEqual as _Ge,
)

from stream.mixins.index import (
    Index as _Index,
    LastIndex as _LastIndex,
    BaseMatchIndexFunc as _BaseMatchIndexFunc,
    MatchIndexFunc as _MatchIndexFunc,
)
from stream.typing import (
    Function as _Function,
    T_co as _T_co,
)


class BaseFilterIndex(
    _Function[_T_co, _T_co],
    _BaseMatchIndexFunc,
):
    def __call__(self, iterable: _typing.Iterable[_T_co]) -> _typing.Iterator[_T_co]:
        index = 0
        for item in iterable:
            if self.ended(index):
                break
            if self.match_index(index):
                yield item
            index += 1

    def __invert__(self):
        return FilterIndex(~self.match_index_f)

    def __and__(self, other: 'BaseFilterIndex'):
        return FilterIndex(
            self.match_index_f & other.match_index_f,
            ended=self.ended_f | other.ended_f,
        )

    def __or__(self, other: 'BaseFilterIndex'):
        return FilterIndex(
            self.match_index_f | other.match_index_f,
            ended=self.ended_f & other.ended_f,
        )


class FilterIndex(
    BaseFilterIndex[_T_co],
    _MatchIndexFunc,
):
    def __init__(
            self,
            match: _Index,
            *,
            ended: _LastIndex = None,
    ):
        _MatchIndexFunc.__init__(self, match, ended=ended)


class Since(BaseFilterIndex[_T_co]):
    def __init__(self, m: int):
        self.__m = m

    @property
    def m(self) -> int:
        return self.__m

    @cached_property
    def match_index_f(self) -> _BaseLogicalFunction:
        return _Ge(self.m)

    @cached_property
    def ended_f(self) -> _BaseLogicalFunction:
        return _false

    def match_index(self, index: int) -> bool:
        return index >= self.m

    def ended(self, index: int) -> bool:
        return False


class Head(BaseFilterIndex[_T_co]):
    def __init__(self, n: int):
        self.__n = n

    @property
    def n(self) -> int:
        return self.__n

    @cached_property
    def match_index_f(self) -> _BaseLogicalFunction:
        return _Lt(self.n)

    @cached_property
    def ended_f(self) -> _BaseLogicalFunction:
        return _Ge(self.n)

    def match_index(self, index: int) -> bool:
        return index < self.n

    def ended(self, index: int) -> bool:
        return index >= self.n
