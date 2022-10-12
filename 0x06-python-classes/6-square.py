#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = (size)
        self.__position = (position)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an iteger")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not ((type(value) is tuple)
                and (a >= 0 and b >= 0 for a, b in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            a, b = self.__position
            for _ in range(self.__size):
                print(' ' * a, end='')
                print('#' * self.__size)
