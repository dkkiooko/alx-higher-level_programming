#!/usr/bin/python3
class Square:
    '''
    class Square defines a square

    Attributes
    ----------
    size : int
        size defines the dimension of edge of square
    '''
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an iteger")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
