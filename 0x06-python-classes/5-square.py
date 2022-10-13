#!/usr/bin/python3
class Square:
    """class that generates Square object
    """
    def __init__(self, size=0):
        """initialize a Square object

        Args:
            size (int, optional): edge of Square. Defaults to 0.
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
            value (int): size of edge of Square object

        Raises:
            TypeError: size is not an integer
            ValueError: size is not positive
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """finds area of a Square object

        Returns:
            int: area of Square
        """
        return self.__size**2

    def my_print(self):
        """prints a square of # of size __size
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size, end='')
                print()
