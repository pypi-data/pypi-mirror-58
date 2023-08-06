import typing as _typing

from stream.mixins.each import (
    BaseItemFunc as _BaseItemFunc,
    ItemFunc as _ItemFunc,
)
from stream.typing import (
    Function as _Function,
    T_co as _T_co,
    V_co as _V_co,
)
from stream.util.func.partial import (
    PartialFunc as _PartialFunc,
)


class BaseOneToOneFunction(
    _Function[_T_co, _V_co],
    _BaseItemFunc[_T_co, _V_co],
):
    def __call__(self, iterable: _typing.Iterable[_T_co]) -> _typing.Iterator[_V_co]:
        for item in iterable:
            yield self.each(item)


class ApplyEach(
    BaseOneToOneFunction[_T_co, _V_co],
    _ItemFunc[_T_co, _V_co],
):
    """
    Apply `func` to all items in the iterable.
    `func` must take each item as the first argument, and then take *args, **kwargs
    """

    def __init__(self, func, *args, **kwargs):
        func = _PartialFunc(func, *args, **kwargs)
        _ItemFunc.__init__(self, func)
