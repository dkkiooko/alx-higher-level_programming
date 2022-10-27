#!/usr/bin/python3
"""extend the student class
"""


class Student:
    """creates a Student
    """
    def __init__(self, first_name, last_name, age):
        """initiates Student

        Args:
            first_name (_str_): _common name_
            last_name (_str_): _surname_
            age (_int_): _physical age_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets attributes

        Args:
            attrs (_list_, optional): attributes to check. Defaults to None.

        Returns:
            _dict_: key value pairs of attributes
        """
        if attrs is None:
            return self.__dict__
        in_list = set(attrs).intersection(self.__dict__.keys())
        return {k: self.__dict__.get(k) for k in in_list}
