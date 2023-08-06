import typing as _typing

from logical import (
    BaseFunction as _BaseLogicalFunction,
    Function as _LogicalFunction,
)

from stream.typing import (
    T_co as _T_co,
)

Match = _typing.Callable[[_T_co], bool]


class BaseMatchFunc(_typing.Generic[_T_co]):
    @property
    def match_f(self) -> _BaseLogicalFunction:
        raise NotImplementedError  # pragma: no cover

    def match(self, item: _T_co) -> bool:
        raise NotImplementedError  # pragma: no cover


class MatchFunc(BaseMatchFunc[_T_co]):
    def __init__(self, match: Match):
        self.__match = _LogicalFunction.get(match)

    @property
    def match_f(self) -> _BaseLogicalFunction:
        return self.__match

    def match(self, item: _T_co) -> bool:
        return self.match_f(item)
