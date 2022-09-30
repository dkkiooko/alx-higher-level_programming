#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new_matris = [[i**2 for i in row] for row in matrix]
    return new_matris
