# -*- coding: utf-8 -*-
from dateutil.parser import parse
from guillotina import configure
from guillotina.component import ComponentLookupError
from guillotina.component import get_adapter
from guillotina.exceptions import ValueDeserializationError
from guillotina.interfaces import IJSONToValue
from guillotina.schema._bootstrapinterfaces import IFromUnicode
from guillotina.schema.exceptions import ValidationError
from guillotina.schema.interfaces import IBool
from guillotina.schema.interfaces import IDate
from guillotina.schema.interfaces import IDatetime
from guillotina.schema.interfaces import IDict
from guillotina.schema.interfaces import IField
from guillotina.schema.interfaces import IFrozenSet
from guillotina.schema.interfaces import IJSONField
from guillotina.schema.interfaces import IList
from guillotina.schema.interfaces import IObject
from guillotina.schema.interfaces import ISet
from guillotina.schema.interfaces import ITuple
from guillotina.schema.interfaces import IUnionField
from zope.interface import Interface

import datetime


def schema_compatible(value, schema_or_field, context=None):
    """The schema_compatible function converts any value to guillotina.schema
    compatible data when possible, raising a TypeError for unsupported values.
    This is done by using the ISchemaCompatible converters.
    """
    if value is None:
        return value

    try:
        return get_adapter(schema_or_field, IJSONToValue, args=[value, context])
    except ComponentLookupError:
        raise ValueDeserializationError(schema_or_field, value, "Deserializer not found for field")


@configure.value_deserializer(Interface)
def default_value_converter(schema, value, context=None):
    if value == {}:
        return {}

    if type(value) != dict:
        return value

    keys = [k for k in value.keys()]
    values = [k for k in value.values()]
    values = [schema_compatible(values[idx], schema[keys[idx]], context) for idx in range(len(keys))]
    return dict(zip(keys, values))


@configure.value_deserializer(IJSONField)
def json_dict_converter(schemafield, value, context=None):
    if value == {}:
        return {}

    return value


@configure.value_deserializer(for_=IField)
def default_converter(field, value, context=None):
    return value


@configure.value_deserializer(IBool)
def bool_converter(field, value, context=None):
    return bool(value)


@configure.value_deserializer(IFromUnicode)
def from_unicode_converter(field, value, context=None):
    return field.from_unicode(value)


@configure.value_deserializer(IList)
def list_converter(field, value, context=None):
    if not isinstance(value, list):
        raise ValueDeserializationError(field, value, "Not an array")
    try:
        return [schema_compatible(item, field.value_type, context) for item in value]
    except ValidationError as error:
        raise ValueDeserializationError(field, value, "Wrong contained type", errors=[error])


@configure.value_deserializer(ITuple)
def tuple_converter(field, value, context=None):
    if not isinstance(value, list):
        raise ValueDeserializationError(field, value, "Not an array")
    return tuple(list_converter(field, value, context))


@configure.value_deserializer(ISet)
def set_converter(field, value, context=None):
    if not isinstance(value, list):
        raise ValueDeserializationError(field, value, "Not an array")
    return set(list_converter(field, value, context))


@configure.value_deserializer(IFrozenSet)
def frozenset_converter(field, value, context=None):
    if not isinstance(value, list):
        raise ValueDeserializationError(field, value, "Not an array")
    return frozenset(list_converter(field, value, context))


@configure.value_deserializer(IDict)
def dict_converter(field, value, context=None):
    if value == {}:
        return {}

    if not isinstance(value, dict):
        raise ValueDeserializationError(field, value, "Not an object")

    try:
        keys, values = zip(*value.items())
        keys = [schema_compatible(keys[idx], field.key_type, context) for idx in range(len(keys))]
        values = [schema_compatible(values[idx], field.value_type, context) for idx in range(len(values))]
        return dict(zip(keys, values))
    except ValidationError as error:
        raise ValueDeserializationError(field, value, "Wrong contained type", errors=[error])


@configure.value_deserializer(IDatetime)
def datetime_converter(field, value, context=None):
    if not isinstance(value, str):
        raise ValueDeserializationError(field, value, "Not a string")
    return parse(value)


@configure.value_deserializer(IDate)
def date_converter(field, value, context=None):
    if not isinstance(value, str):
        raise ValueDeserializationError(field, value, "Not a string")
    return datetime.datetime.strptime(value, "%Y-%m-%d").date()


@configure.value_deserializer(IObject)
def object_converter(field, value, context=None):
    if not isinstance(value, dict):
        raise ValueDeserializationError(field, value, "Not an object")
    try:
        result = {}
        for key, val in value.items():
            if key in field.schema:
                f = field.schema[key]
                if val is not None:
                    result[key] = get_adapter(f, IJSONToValue, args=[val, context])
                else:
                    result[key] = None
        return result
    except ValidationError as error:
        raise ValueDeserializationError(field, value, "Wrong contained type", errors=[error])


@configure.value_deserializer(IUnionField)
def union_converter(field, value, context=None):
    for f in field.fields:
        try:
            val = schema_compatible(value, f)
            if f.__implemented__(IObject) and value and not val:
                continue  # IObject doesn't match
            return val
        except Exception:
            pass
    raise ValueDeserializationError(field, value, "Doesn't match any field")
