import typing as _typing
from queue import (
    Queue as _Queue,
    Empty as _Empty,
)
from threading import (
    Thread as _Thread,
)

from gimme_cached_property import cached_property

from stream.typing import (
    Function as _Function,
    T_co as _T_co,
)


class Prefetch(_Function[_T_co, _T_co]):
    """
    Utilize multi-threading to prefetch items in the iterable.
    Useful when both the `next` call and the subsequent processing are time-consuming.
    """

    class Timeout(Exception):
        pass

    def __init__(
            self,
            *,
            n: _typing.Optional[int] = 1,
            timeout: float = None,
    ):
        """
        :param n:
            The desired number of items to prefetch.
            The prefetch thread will keep pre-fetching
            as long as the number of pre-fetched items is smaller than n.
            If None, do not limit.
        :param timeout:
            The timeout for each `next` call, if the prefetch is empty.
            If None, do not limit.
        """
        self.__n = n
        self.__timeout = timeout

    @property
    def _n(self) -> _typing.Optional[int]:
        return self.__n

    @property
    def _timeout(self) -> _typing.Optional[float]:
        return self.__timeout

    @property
    def _maxsize(self) -> int:
        if self._n is None:
            return 0
        return self._n

    @cached_property
    def iterator_class(self) -> _typing.Type[_typing.Iterator[_T_co]]:
        prefetch = self

        class ThreadedPrefetchIterator(_typing.Iterator[_T_co]):
            def __init__(self, iterable: _typing.Iterable[_T_co]):
                self.__iter = iter(iterable)
                self.__queue = _Queue(maxsize=prefetch._maxsize)
                self.__finished = False

                self.__thread = self.thread_class()
                self.__thread.start()

            def _prefetch_one(self) -> None:
                try:
                    item = next(self.__iter)
                except StopIteration:
                    self.__finished = True
                    raise
                self.__queue.put(item)

            @cached_property
            def thread_class(self) -> _typing.Type[_Thread]:
                iterator = self

                class PrefetchThread(_Thread):
                    def run(self) -> None:
                        try:
                            while True:
                                iterator._prefetch_one()
                        except StopIteration:
                            pass

                return PrefetchThread

            def __next__(self) -> _T_co:
                if self.__finished and self.__queue.empty():
                    raise StopIteration

                try:
                    item = self.__queue.get(timeout=prefetch._timeout)
                except _Empty:
                    raise prefetch.Timeout from None
                self.__queue.task_done()
                return item

        return ThreadedPrefetchIterator

    def __call__(self, iterable: _typing.Iterable[_T_co]) -> _typing.Iterator[_T_co]:
        return self.iterator_class(iterable)
