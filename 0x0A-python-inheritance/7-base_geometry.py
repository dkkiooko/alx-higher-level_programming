#!/usr/bin/python3
"""class with integer validation"""


class BaseGeometry:
    """validates an named integer
    """
    def area(self):
        """to be defined later

        Raises:
            Exception: this function is undefined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ensures value is an integer

        Args:
            name (_str_): _descriptor of value_
            value (_int_): _a number_

        Raises:
            TypeError: _value must be an instance int_
            ValueError: _value must be larger than 0_
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
