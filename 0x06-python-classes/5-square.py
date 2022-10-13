#!/usr/bin/python3
class Square:
    '''
    class Square defines a new object

    Args:
        size (int): This is the size of a square

    Attributes:
        __size (int): This is where we store size
    '''
    def __init__(self, size=0):
        self.size = (size)

    @property
    def size(self):
        '''
        This is the getter method for size

        Returns:
            __size: size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        setter method for size

        Raises:
            TypeError: size isnt an integer
            ValueError: size isnt positive
        '''
        if (type(value) is not int):
            raise TypeError("size must be an iteger")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        method finds the area of a Square object

        Returns:
            area of Square object
        '''
        return self.__size**2

    def my_print(self):
        '''
        method prints a square made of
        '''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size, end='')
                print()
