#!/usr/bin/python3
"""module that prints square of #"""


def print_square(size):
    """prints a square

    Args:
        size (int): length of edge of square

    Raises:
        TypeError: size must be integer
        ValueError: size must be positive
        TypeError: size should not be float
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (size < 0) and isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#"*size)
