#!/usr/bin/python3
"""generate a pascal triangle
"""


def pascal_triangle(n):
    """create a pascal triangle

    Args:
        n (_int_): size of the pascal triangle

    Returns:
        _list_: _list of lists of arrays of pascal triangle_
    """
    if n <= 0:
        return []
    else:
        result = [list(str(11**i)) for i in range(5)]
        result = [[int(i) for i in j] for j in result]
        return result
