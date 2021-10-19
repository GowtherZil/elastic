from typing import Dict, List, Optional

from elastic._vars import DEFAULTS, FIELDS, SCHEMA, VALIDATORS
from elastic.fields.base import Field
from elastic.models.meta import MetaModel
from elastic.validators.base import validate as elastic_validate
from elastic.validators.exceptions import ValidationError


class Model(Field, metaclass=MetaModel):
    def __init__(self, **kwargs) -> None:
        super().__init__()

        defaults = getattr(self, DEFAULTS, {}).copy()

        for k in defaults.keys():
            if k in kwargs:
                defaults[k] = kwargs[k]
                del kwargs[k]
            setattr(self, k, defaults[k])

    def validate(self):

        validators = getattr(self, VALIDATORS, {})
        fields: Dict[str, Dict] = validators.get(FIELDS, {})
        schema: Dict = validators.get(SCHEMA, {})

        errors = []

        for field, field_validators in fields.items():
            for valid in field_validators.values():
                error = valid(getattr(self, field, None))
                if error:
                    errors.append(error)

        for valid in schema.values():
            error = valid(self)
            if error:
                errors.append(error)

        if errors:
            raise ValidationError(errors)

        return self

    @elastic_validate
    def strict_type(cls, v):
        return isinstance(v, cls)
