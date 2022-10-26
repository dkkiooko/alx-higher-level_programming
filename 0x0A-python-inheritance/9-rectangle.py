#!/usr/bin/python3
"""create rectangle with str attributes
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry

    Args:
        BaseGeometry (_BaseGeometry_): _base class that validates an integer_
    """
    def __init__(self, width, height):
        """initialize a Rectangle

        Args:
            width (_int_): _length in x_
            height (_int_): _length in y_
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """_find area of rectangle_

        Returns:
            _int_: _(x * y)_
        """
        return self.__width * self.__height

    def __str__(self):
        """ add a str attribute to rectangle

        Returns:
            _str_: _string describing rectangle width/height_
        """
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)
