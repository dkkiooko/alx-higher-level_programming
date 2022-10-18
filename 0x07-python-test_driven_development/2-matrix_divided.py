#!/usr/bin/python3
"""divide a matrix with number
"""


def dim(a):
    """gets shape of matrix

    Args:
        a (list): matrix

    Returns:
        list: every element represents size of dimension
    """
    if not isinstance(a, list):
        return []
    try:
        return [len(a)] + dim(a[0])
    except Exception:
        return []


def matrix_divided(matrix, div):
    """divide matrix with number

    Args:
        matrix (list): list of lists
        div (integer): number to divide

    Raises:
        TypeError: matrix is not list of lists
        TypeError: rows are not same size
        TypeError: must be integers
        ZeroDivisionError: cannot divide with zero

    Returns:
        list: new matrix divided by div
    """
    dimensions = dim(matrix)
    if len(matrix[0]) == 0:
        return [[]]
    if len(dimensions) != 2:
        raise TypeError("matrix must be a matrix \
            (list of lists) or integers/floats")
    if not all((len(matrix[i]) == dimensions[1]
                for i in range(dimensions[0]))):
        raise TypeError("Each row of the matrix \
                            must have the same size")
    if not all((isinstance(i, int) or isinstance(i, float)
                for i in sum(matrix, []))):
        raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = [[round(i/div, 2) for i in row] for row in matrix]
    return new_matrix
