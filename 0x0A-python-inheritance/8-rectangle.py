#!/usr/bin/python3
"""inherit from a base class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry

    Args:
        BaseGeometry (_BaseGeometry_): _base class that validates an integer_
    """
    def __init__(self, width, height):
        """initialize Rectangle

        Args:
            width (_int_): _length in y_
            height (_int_): _length in x_
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
