#!/usr/bin/python3
"""instance of a class
"""


def is_kind_of_class(obj, a_class):
    """chech if obj is an instance of a_class

    Args:
        obj (object): an ojbect with attributes
        a_class (class): eg int, float, Rectangle

    Returns:
        Bool: True if is an instance from a_class
    """
    return isinstance(obj, a_class)
