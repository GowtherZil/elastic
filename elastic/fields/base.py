from typing import Type

from elastic._vars import ELASTIC_BASE, SCHEMA, VALIDATORS
from elastic.fields.descriptor import FieldDescriptor
from elastic.fields.meta import MetaField
from elastic.validators import validate


class Field(metaclass=MetaField):
    @classmethod
    def descriptor(cls, name):
        return FieldDescriptor[getattr(cls, ELASTIC_BASE)](name)

    @validate
    def not_none(cls, v):
        return v is not None

    @validate
    def strict_type(cls, v):
        return isinstance(v, getattr(cls, ELASTIC_BASE))


def Optional(field: Type[Field]):
    not_none = lambda cls, x: True
    not_none.__name__ = "not_none"

    return type(f"Optional{field.__name__}", (field,), {"not_none": validate(not_none)})


def Dynamic(field: Type[Field]):

    strict_type = lambda cls, x: True
    strict_type.__name__ = "strict_type"

    return type(
        f"Dynamic{field.__name__}", (field,), {"strict_type": validate(strict_type)}
    )
