import typing as _typing

from gimme_cached_property import cached_property
from logical import (
    BaseFunction as _BaseLogicalFunction,
    Function as _LogicalFunction,
)
from logical.boolean import (
    false as _false,
)
from logical.collection import (
    In as _In,
)
from logical.comparison import (
    Equal as _Equal,
    GreaterThanOrEqual as _Ge,
    GreaterThan as _Gt,
)

MatchIndex = _typing.Callable[[int], bool]
Index = _typing.Union[
    int,
    _typing.Collection[int],
    MatchIndex,
]
LastIndex = _typing.Union[
    int,
    MatchIndex,
]


class BaseMatchIndexFunc(object):
    @property
    def match_index_f(self) -> _BaseLogicalFunction:
        raise NotImplementedError  # pragma: no cover

    @property
    def ended_f(self) -> _BaseLogicalFunction:
        raise NotImplementedError  # pragma: no cover

    def match_index(self, index: int) -> bool:
        raise NotImplementedError  # pragma: no cover

    def ended(self, index: int) -> bool:
        raise NotImplementedError  # pragma: no cover


class MatchIndexFunc(BaseMatchIndexFunc):
    def __init__(
            self,
            match: Index,
            *,
            ended: LastIndex = None,
    ):
        self.__match = match
        self.__ended = ended

    @cached_property
    def match_index_f(self) -> _BaseLogicalFunction:
        if isinstance(self.__match, int):
            return _Equal(self.__match)
        elif isinstance(self.__match, _typing.Collection):
            return _In(self.__match)
        else:
            return _LogicalFunction.get(self.__match)

    @cached_property
    def _ended_f(self) -> _BaseLogicalFunction:
        if isinstance(self.__ended, int):
            return _Ge(self.__ended)
        else:
            return _LogicalFunction.get(self.__ended)

    @cached_property
    def _ended_f_match(self) -> _BaseLogicalFunction:
        if isinstance(self.__match, int):
            return _Gt(self.__match)
        elif isinstance(self.__match, _typing.Collection):
            return _Gt(max(self.__match))
        else:
            return _false

    @cached_property
    def ended_f(self) -> _BaseLogicalFunction:
        if self.__ended is not None:
            return self._ended_f
        else:
            return self._ended_f_match

    def match_index(self, index: int) -> bool:
        return self.match_index_f(index)

    def ended(self, index: int) -> bool:
        return self.ended_f(index)
