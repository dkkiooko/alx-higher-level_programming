#!/usr/bin/python3
"""square inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square inherits from rectangle

    Args:
        Rectangle (_Rectangle_): _class with height, width and str attribute_
    """
    def __init__(self, size):
        """initialize a Square object

        Args:
            size (_int_): _dimension of the square_
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
