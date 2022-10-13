#!/usr/bin/python3
class Square:
    """class Square

    Attributes
    ----------
        size : int
            Dimension of a Square object

    Raises:
        TypeError: size must be an integer
        ValueError: size must be positive
    """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an iteger")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        calculates the area of Square object

        Returns:
            size**2: area
        '''
        return self.__size**2
