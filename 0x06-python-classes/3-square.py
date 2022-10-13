#!/usr/bin/python3
class Square:
    """class that generates a Square
    """
    def __init__(self, size=0):
        """initalize a size object

        Args:
            size (int, optional): edge of square. Defaults to 0.

        Raises:
            TypeError: size is not an integer
            ValueError: size is not positive
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """find area of square

        Returns:
            int: square of Square object
        """
        return self.__size**2
