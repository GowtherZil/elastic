from elastic._vars import DEFAULTS, FIELDS, SCHEMA, VALIDATORS
from elastic.fields.base import Field
from elastic.fields.meta import MetaField
from elastic._utils import BoundMethod
from elastic.validators import FieldValidator


class MetaModel(MetaField):
    def __new__(cls, name: str, bases: tuple, attrs: dict):
        newtype = super().__new__(cls, name, bases, attrs, base=object)

        # building up the fields validator and defaults holders
        fields = {}
        defaults = {}

        for b in bases:
            # updating fields from bases
            validators = getattr(b, VALIDATORS, {})

            # manual or
            for k, v in validators.get(FIELDS, {}):
                # check here if is bounded class metaclass is not a  MetaField
                if not type(getattr(v, "bounded_class")) == MetaField:
                    setattr(v, "bounded_class", newtype)
                fields[k] = v

            # updating defaults from base
            defaults = defaults | getattr(b, DEFAULTS, {})

        # searching for field validators on class attributes
        for name, field in attrs.items():
            if isinstance(field, FieldValidator):
                if field.field in fields:
                    fields[field.field][name] = BoundMethod(newtype, field)
                else:
                    fields[field.field] = {name: BoundMethod(newtype, field)}

        # working with annotations
        for aname, atype in attrs.get("__annotations__", {}).items():

            # setting up defaults
            if aname in attrs:
                defaults[aname] = attrs[aname]
            else:
                defaults[aname] = None

            # setting up field descriptors
            if issubclass(atype, Field):
                setattr(newtype, aname, atype.descriptor(aname))
                fv = getattr(atype, VALIDATORS, {}).get(SCHEMA, {})

                if aname in fields:
                    # ensuring overriden
                    fields[aname] = fv | fields[aname]
                else:
                    fields[aname] = fv

        # setting field validators
        validators = getattr(newtype, VALIDATORS, {})
        validators[FIELDS] = fields

        # setting defaults
        setattr(newtype, DEFAULTS, defaults)

        # done
        return newtype
