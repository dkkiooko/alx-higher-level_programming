#!/usr/bin/python3
"""get list of available attributes
"""


def lookup(obj):
    """returns a list of attributes

    Args:
        obj (object): an object
    """
    return dir(obj)
