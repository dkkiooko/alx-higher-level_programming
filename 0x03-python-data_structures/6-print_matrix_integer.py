#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for elements in element:
            print(f"{elements:d}", end=" ")
        print('\n')
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print_matrix_integer(matrix)