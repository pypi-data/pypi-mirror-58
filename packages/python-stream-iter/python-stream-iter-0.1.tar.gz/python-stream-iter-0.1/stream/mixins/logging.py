import typing as _typing

from stream.typing import (
    T_co as _T_co,
)

LogFunc = _typing.Callable[[str], None]
Formatter = _typing.Callable[[_T_co], str]


class BaseLogItemFunc(_typing.Generic[_T_co]):
    def log_msg(self, msg: str) -> None:
        raise NotImplementedError  # pragma: no cover

    def format(self, item: _T_co) -> str:
        raise NotImplementedError  # pragma: no cover

    def log(self, item: _T_co) -> None:
        self.log_msg(self.format(item))


class LogItemFunc(BaseLogItemFunc[_T_co]):
    def __init__(
            self,
            log_func: LogFunc,
            formatter: Formatter,
    ):
        self.__log_func = log_func
        self.__formatter = formatter

    @property
    def log_msg_f(self) -> LogFunc:
        return self.__log_func

    def log_msg(self, msg: str) -> None:
        self.log_msg_f(msg)

    @property
    def format_f(self) -> Formatter:
        return self.__formatter

    def format(self, item: _T_co) -> str:
        return self.format_f(item)
