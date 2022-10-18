#!/usr/bin/python3
"""module that adds 2 integers
"""


def add_integer(a, b=98):
    """add 2 integers

    Args:
        a (int): number to add
        b (int, optional): number to be added. Defaults to 98.

    Raises:
        TypeError: a is not an integer
        TypeError: b is not an integer

    Returns:
        int: sum of a and b
    """
    if (not isinstance(a, (int, float))) or (a is None):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))) or (b is None):
        raise TypeError("b must be an integer")
    return int(a)+int(b)
