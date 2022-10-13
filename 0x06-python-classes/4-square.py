#!/usr/bin/python3
class Square:
    """class that defines a Square object
    """
    def __init__(self, size=0):
        """initialize a Square object

        Args:
            size (int, optional): edge of square. Defaults to 0.
        """
        self.size = (size)

    @property
    def size(self):
        """getter method for size

        Returns:
            int: size of edge of Square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size

        Args:
            value (int): edge of Square object

        Raises:
            TypeError: value is not integer
            ValueError: value is not positive
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """find area of Square object

        Returns:
            int: square of Square object
        """
        return self.__size**2
