#!/usr/bin/python3
"""add attribute to object
"""


def add_attribute(obj, objname, value):
    """add attribute to object

    Args:
        obj (_object_): _a python object_
        objname (_str_): _name of new attribute_
        value (_str/int_): _value to store in new attribute_

    Raises:
        TypeError: _if object doesn't allow to add attribute_
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
