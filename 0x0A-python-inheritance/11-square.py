#!/usr/bin/python3
"""give square a str attribute"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle

    Args:
        Rectangle (_Rectangle_): _class with (x,y) dimensions_
    """
    def __init__(self, size):
        """initialize a Square object

        Args:
            size (_int_): _dimension of the object_
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """str attribute for Square

        Returns:
            _str_: _describes shape and length of side of obj_
        """
        return f"[Square] {self.__size}/{self.__size}"
