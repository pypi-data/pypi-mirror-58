import csv as _csv
import typing as _typing

from stream.typing import (
    Function as _Function,
)
from .collections import (
    ToDict as _ToDict,
)
from .each import (
    BaseOneToOneFunction as _BaseOneToOneFunction,
)

CsvRow = _typing.List[str]


class Csv(_BaseOneToOneFunction[str, CsvRow]):
    def __init__(self, *args, **kwargs):
        """
        :param args: and
        :param kwargs:
            See csv.reader
        """
        self.__args = args
        self.__kwargs = kwargs

    def each(self, item: str) -> CsvRow:
        return next(_csv.reader([item], *self.__args, **self.__kwargs))


class CsvToDict(_Function[_typing.Sequence, _typing.Dict]):
    """
    Use the first row as keys.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs: See collections.ToDict
        """
        self.__kwargs = kwargs

    def __call__(
            self,
            iterable: _typing.Iterable[_typing.Sequence],
    ) -> _typing.Iterator[_typing.Dict]:
        iterable = iter(iterable)
        keys = next(iterable)
        to_dict = _ToDict(*keys, **self.__kwargs)
        yield from to_dict(iterable)
