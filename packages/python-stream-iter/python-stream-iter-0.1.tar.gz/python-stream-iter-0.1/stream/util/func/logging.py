import logging as _logging
import typing as _typing


class LoggerLog(object):
    def __init__(
            self,
            logger: _typing.Union[_logging.Logger, str],
            *,
            level: int,
    ):
        if isinstance(logger, str):
            logger = _logging.getLogger(logger)
        self.__logger = logger
        self.__level = level

    @property
    def logger(self) -> _logging.Logger:
        return self.__logger

    @property
    def level(self) -> int:
        return self.__level

    def __call__(self, msg: str) -> None:
        self.logger.log(
            level=self.level,
            msg=msg,
        )
