from dataclasses import dataclass
from typing import Any, Callable, Type


@dataclass
class BoundMethod:
    bounded_class: Type
    bounded_method: Callable[[Type, Any], bool]

    def __call__(self, v) -> bool:
        return self.bounded_method(self.bounded_class, v)
