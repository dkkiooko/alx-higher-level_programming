#!/usr/bin/python3
"""module that compares type
"""


def is_same_class(obj, a_class):
    """find class of object

    Args:
        obj (object): an object with attributes
        a_class (class): class eg int or float

    Returns:
        bool: True if object is of class a_class... False
    """
    return type(obj) == a_class
