#!/usr/bin/python3
class Square:
    '''
    class Square

    Args:
        size (int): size of the class Square
        position (int): tuple that shows position of square
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = (size)
        self.__position = (position)

    @property
    def size(self):
        '''
        getter method for size

        Returns:
            __size: size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        setter method for size

        Args:
            value (int): size of class Square
        '''
        if (type(value) is not int):
            raise TypeError("size must be an iteger")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''
        getter method for position

        Returns:
            __position: tuple of position
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        setter method for position

        Raises:
            TypeError: position is not a tuple of 2 integers
        '''
        if not ((type(value) is tuple)
                and (a >= 0 and b >= 0 for a, b in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''
        method to calculate area

        Returns: area of square
        '''
        return self.__size**2

    def my_print(self):
        '''
        method that prints out a square made of #
        '''
        if self.__size == 0:
            print()
        else:
            a, b = self.__position
            for _ in range(self.__size):
                print(' ' * a, end='')
                print('#' * self.__size)
