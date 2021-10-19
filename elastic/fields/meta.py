from functools import partial
from typing import Dict, Type

from elastic._vars import ELASTIC_BASE, SCHEMA, VALIDATORS
from elastic._utils import BoundMethod
from elastic.validators.base import FieldValidator, SchemeValidator


class MetaField(type):
    def __new__(cls, name: str, bases: tuple, attrs: dict, base: Type = object):
        # build new type
        new_type = super().__new__(cls, name, bases, attrs)

        # cretae schema validator holder
        schema = {}

        # update schema from bases
        for b in bases:
            validators:Dict[str, BoundMethod] = getattr(b, VALIDATORS, {}).get(SCHEMA, {})
            # a manual or
            for key, v in validators.items():
                schema[key] = BoundMethod(new_type, v.bounded_method )

        # update schema from fields
        for name, field in attrs.items():

            if isinstance(field, FieldValidator):
                continue

            if isinstance(field, SchemeValidator):
                schema[name] = BoundMethod(new_type, field)

        # add validators to attrs
        setattr(new_type, VALIDATORS, {SCHEMA: schema})
        setattr(new_type, ELASTIC_BASE, base)

        # return new type
        return new_type
