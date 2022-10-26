#!/usr/bin/python3
"""check whether obj is a subclass
"""


def inherits_from(obj, a_class):
    """check for inheritance

    Args:
        obj (object): class object
        a_class (name): name of a class

    Returns:
        Bool: True if obj inherits from a_class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
