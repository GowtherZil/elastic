from typing import Generic, Type, TypeVar

from elastic._vars import RAW_DATA

T = TypeVar("T")


class FieldDescriptor(Generic[T]):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __get__(self, instance, owner: Type = None) -> T:
        return getattr(instance, RAW_DATA, {}).get(self.name, None)

    def __set__(self, instance, value: T):
        try:
            getattr(instance, RAW_DATA)[self.name] = value
        except AttributeError:
            setattr(instance, RAW_DATA, {self.name: value})

    def __delete__(self, instance):
        try:
            del getattr(instance, RAW_DATA)[self.name]
        except AttributeError:
            pass
        except KeyError:
            pass
        except:
            pass
