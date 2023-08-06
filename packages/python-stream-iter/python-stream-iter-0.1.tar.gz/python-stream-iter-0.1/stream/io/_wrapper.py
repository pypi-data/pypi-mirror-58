import typing as _typing

from gimme_cached_property import cached_property

from . import (
    File as _File,
    TextFile as _TextFile,
    BinaryFile as _BinaryFile,
)

FileType = _typing.TypeVar('FileType', bound=_File)
TextFileType = _typing.TypeVar('TextFileType', bound=_TextFile)
BinaryFileType = _typing.TypeVar('BinaryFileType', bound=_BinaryFile)


def wrapper_class(
        wrapped_class: _typing.Union[_typing.Type, _typing.Callable],
        *,
        file_class: _typing.Type[FileType] = _File,
) -> _typing.Type[FileType]:
    class WrapperClass(file_class):
        def __init__(self, *args, **kwargs):
            self._wrapped = wrapped_class(*args, **kwargs)

        def __enter__(self) -> 'WrapperClass':
            self._wrapped.__enter__()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            return self._wrapped.__exit__()

        def __next__(self):
            return next(self._wrapped)

        def __iter__(self):
            return iter(self._wrapped)

        def __getattribute__(self, name: str):
            """
            1. If in __dict__, return it;
            2. If defined in subclasses of file_class, use it;
            3. Try get attr of wrapped object;
            4. Use definition from file_class.
            """
            if name in ['__dict__', '__class__']:
                return object.__getattribute__(self, name)
            if name in self.__dict__:
                # is a variable
                return object.__getattribute__(self, name)

            try:
                this_attr = object.__getattribute__(self, name)
            except (AttributeError, NotImplementedError) as e:
                return getattr(self._wrapped, name)

            if name in self.__dict__:
                # cached_property
                return this_attr

            cls_attr = getattr(self.__class__, name)
            try:
                super_cls_attr = getattr(file_class, name)
            except AttributeError:
                return this_attr

            if cls_attr != super_cls_attr:
                return this_attr

            try:
                return getattr(self._wrapped, name)
            except AttributeError:
                return this_attr

    return WrapperClass


def buffer_class(
        file: _File,
        *,
        file_class: _typing.Type[BinaryFileType] = _BinaryFile,
) -> _typing.Type[BinaryFileType]:
    class BufferClass(binary_wrapper_class(lambda: file._wrapped.buffer, file_class=file_class)):
        _text_file = file

        def __init__(self):
            # no param
            super().__init__()

        def __eq__(self, other: _File):
            if isinstance(other, BufferClass):
                return True
            if not hasattr(other, '_text_file'):
                return False
            return self._text_file == other._text_file

        def __exit__(self, exc_type, exc_val, exc_tb):
            # don't close
            pass

    return BufferClass


def text_wrapper_class(
        wrapped_class: _typing.Union[_typing.Type, _typing.Callable],
        *,
        file_class: _typing.Type[TextFileType] = _TextFile,
) -> _typing.Type[TextFileType]:
    class TextWrapperClass(wrapper_class(wrapped_class, file_class=file_class)):
        @cached_property
        def _buffer_class(self) -> _typing.Type[_BinaryFile]:
            return buffer_class(self)

        @property
        def buffer(self) -> _BinaryFile:
            return self._buffer_class()

    return TextWrapperClass


def binary_wrapper_class(
        wrapped_class: _typing.Union[_typing.Type, _typing.Callable],
        *,
        file_class: _typing.Type[BinaryFileType] = _BinaryFile,
) -> _typing.Type[BinaryFileType]:
    class BinaryWrapperClass(wrapper_class(wrapped_class, file_class=file_class)):
        pass

    return BinaryWrapperClass
