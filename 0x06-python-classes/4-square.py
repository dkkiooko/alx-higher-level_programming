#!/usr/bin/python3
class Square:
    '''
    this is class Square

    Attributes:
        size (int): the size of an integer
    '''
    def __init__(self, size=0):
        self.size = (size)

    @property
    def size(self):
        '''
        getter method for Square object

        Returns:
            the size of Square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        setter method for Square object

        Args:
            value (int): value to set as size of Square object

        Raises:
            TypeError: size isnt integer
            ValueError: size is not positive
        '''
        if (type(value) is not int):
            raise TypeError("size must be an iteger")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        get the area of a Square object

        Returns:
            area of the Square object
        '''
        return self.__size**2
