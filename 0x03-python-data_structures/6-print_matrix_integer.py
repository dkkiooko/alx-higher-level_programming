#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for element in matrix:
            for i in range(len(element)):
                if i ==  len(element) - 1:
                    print("{:d}".format(element[i]), end="")
                else:
                    print("{:d}".format(element[i]), end=" ")
            print()
