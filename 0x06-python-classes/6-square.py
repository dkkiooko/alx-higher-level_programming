#!/usr/bin/python3
class Square:
    """class that generates a Square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize a Square object

        Args:
            size (int, optional): edge of square. Defaults to 0.
            position (tuple, optional): x,y coordinates. Defaults to (0, 0).
        """
        self.__size = (size)
        self.__position = (position)

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
            value (int): size of edge of square

        Raises:
            TypeError: size is not an integer
            ValueError: size is negative
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter method for positions

        Returns:
            tuple: x,y coordinates of Square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position of Square object

        Args:
            value (tuple): x,y coordinate of Square object

        Raises:
            TypeError: value isnt a tuple of 2 positive integers
        """
        if not ((type(value) is tuple)
                and (a >= 0 and b >= 0 for a, b in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """gets area of Square object

        Returns:
            int: area of Square object
        """
        return self.__size**2

    def my_print(self):
        """prints a square on the screen
        """
        if self.__size == 0:
            print()
        else:
            a, b = self.__position
            for _ in range(self.__size):
                print(' ' * a, end='')
                print('#' * self.__size)
