import sys as _sys

from . import (
    _wrapper,
)


class StdIn(_wrapper.text_wrapper_class(lambda: _sys.stdin)):
    def __init__(self):
        # no param
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, StdIn)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # don't close
        pass


class StdOut(_wrapper.text_wrapper_class(lambda: _sys.stdout)):
    def __init__(self):
        # no param
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, StdOut)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Don't close
        pass


class StdErr(_wrapper.text_wrapper_class(lambda: _sys.stderr)):
    def __init__(self):
        # no param
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, StdErr)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # don't close
        pass


stdin = StdIn()
stdout = StdOut()
stderr = StdErr()
