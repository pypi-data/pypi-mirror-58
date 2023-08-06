class PartialFunc(object):
    def __init__(self, func, *args, **kwargs):
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self, item):
        return self.__func(item, *self.__args, **self.__kwargs)

    @staticmethod
    def get(func, *args, **kwargs):
        if not args and not kwargs:
            return func
        return PartialFunc(func, *args, **kwargs)
