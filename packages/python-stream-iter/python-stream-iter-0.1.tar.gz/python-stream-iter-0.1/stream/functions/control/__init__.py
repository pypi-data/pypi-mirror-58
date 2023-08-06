import typing as _typing

from stream.typing import (
    Function as _Function,
    T_co as _T_co,
)


class Preload(_Function[_T_co, _T_co]):
    """
    Preload a number of items in the beginning.
    """

    def __init__(
            self,
            *,
            n: _typing.Optional[int] = 1,
            not_enough_error: _typing.Union[
                bool,
                _typing.Type[Exception],
            ] = False,
    ):
        """
        :param n:
            Number of entries to preload.
            Default: 1.
            If None, preload all items.
        :param not_enough_error:
            If False (default), simply yield all entries;
            If True, raise StopIteration;
            Otherwise, raise not_enough_error().
        """
        self.__n = n
        self.__error = not_enough_error

    def __call__(self, iterable: _typing.Iterable[_T_co]) -> _typing.Iterator[_T_co]:
        if self.__n is None:
            return self.__preload_all(iterable)

        iterator = iter(iterable)
        preloaded = []

        while len(preloaded) < self.__n:
            try:
                preloaded.append(next(iterator))
            except StopIteration:
                if not self.__error:
                    return iter(preloaded)
                elif self.__error is True:
                    raise
                else:
                    raise self.__error() from None

        def __generator():
            yield from preloaded
            yield from iterator

        return __generator()

    @staticmethod
    def __preload_all(iterable: _typing.Iterable[_T_co]) -> _typing.Iterator[_T_co]:
        preloaded = tuple(iterable)
        return iter(preloaded)
