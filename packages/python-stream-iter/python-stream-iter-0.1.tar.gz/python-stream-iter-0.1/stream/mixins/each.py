import typing as _typing

from stream.typing import (
    T_co as _T_co,
    V_co as _V_co,
)

Each = _typing.Callable[[_T_co], _V_co]


class BaseItemFunc(_typing.Generic[_T_co, _V_co]):
    def each(self, item: _T_co) -> _V_co:
        raise NotImplementedError  # pragma: no cover


class ItemFunc(BaseItemFunc[_T_co, _V_co]):
    def __init__(self, func: Each):
        self.__func = func

    @property
    def each_f(self) -> Each:
        return self.__func

    def each(self, item: _T_co) -> _V_co:
        return self.each_f(item)
