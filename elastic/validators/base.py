from abc import ABCMeta, abstractmethod
from functools import partial, update_wrapper
from typing import Any, Callable

# TODO: Validators as a class method


class Validator(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, value):
        pass


class SchemeValidator(Validator):
    def __init__(self, f: Callable[[Any], bool]) -> None:
        super().__init__()
        self._f = f
        update_wrapper(self, self._f)

    def message_text_alternative(self):
        return 'Validator "{validator}" fail with value "{value}" on "{model}".'

    def message_text(self):
        return (
            self._f.__doc__
            if self._f.__doc__ is not None
            else self.message_text_alternative()
        )

    def context(self):
        return {"validator": self._f.__name__}

    def __call__(self, cls, value):
        if not self._f(cls, value):
            return self.message_text().format(
                **({"value": value, "model": cls.__name__} | self.context())
            )

    def __str__(self) -> str:
        return self._f.__name__


class FieldValidator(SchemeValidator):
    def __init__(
        self,
        field: str,
        f: Callable[[Any], bool],
    ) -> None:
        super().__init__(f)
        self._field = field

    @property
    def field(self):
        return self._field

    def message_text_alternative(self):
        return 'Validator "{validator}" fail with value "{value}" on model "{model}" on field "{field}".'

    def context(self):
        return super().context() | {"field": self.field}


def validate(field=None):
    """A decorator to make validators from functions

    Parameters
    ----------
    field : Callable[cls, Any], optional
        The function to turn a callable into a validator, by default None.
        This functin can have a docstring with this context vars:
        'model', 'field', 'value', 'validator'.
        This docstring will be used to build error messages.

    Returns
    -------
    Validator
    """
    if callable(field):
        return SchemeValidator(field)
    else:
        return partial(FieldValidator, field)
