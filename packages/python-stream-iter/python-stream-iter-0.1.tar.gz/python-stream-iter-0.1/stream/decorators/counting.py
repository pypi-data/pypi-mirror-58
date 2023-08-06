import typing as _typing

from stream.functions.counting import (
    Report as _Report,
    Log as _Log,
)
from . import (
    from_function as _from_function,
)

report = _from_function(_Report, has_params=True)


class log(object):
    __self = _from_function(_Log, has_params=True)

    """
    Log progress of a generator
    """

    def __init__(
            self,
            *,
            log_func: _typing.Callable[[str], None] = print,
            name=None,
            interval=1000,
    ):
        self.__log = log_func
        self.__name = name
        self.__interval = interval

    def __call__(self, gen):
        name = self.__name or gen.__name__
        return self.__self(
            log_func=self.__log,
            name=name,
            interval=self.__interval,
        )(gen)
