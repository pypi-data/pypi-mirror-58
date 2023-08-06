from functools import wraps

from gimme_cached_property import cached_property

from stream.typing import Function


class from_function(object):
    """
    Change a iterator function to a generator decorator
    """

    def __init__(self, func: Function, *, has_params: bool):
        self.__func = func
        self.__doc__ = func.__doc__
        self.__has_params = has_params

    @property
    def _func(self) -> Function:
        return self.__func

    @property
    def _has_params(self) -> bool:
        return self.__has_params

    @cached_property
    def callable_class(self):
        decorator = self

        class NewFunc(object):
            def __init__(self, *args, **kwargs):
                if decorator._has_params:
                    self.__f = decorator._func(*args, **kwargs)
                else:
                    self.__f = decorator._func

            def __call__(self, gen):
                @wraps(gen)
                def __new_gen(*args, **kwargs):
                    return self.__f(gen(*args, **kwargs))

                return __new_gen

        return NewFunc

    def __call__(self, *args, **kwargs):
        if self._has_params:
            return self.callable_class(*args, **kwargs)
        else:
            return self.callable_class()(args[0])
