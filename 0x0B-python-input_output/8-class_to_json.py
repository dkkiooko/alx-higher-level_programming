#!/usr/bin/python3
"""get attributes of an object"""


def class_to_json(obj):
    """gets attributes of an object

    Args:
        obj (_object_): _object eg class, type with attributes_

    Returns:
        _list_: _of attributes_
    """
    return vars(obj)
