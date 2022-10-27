#!/usr/bin/python3
"""module that creates a Student
"""


class Student:
    """creates a Student with a few properties
    """
    def __init__(self, first_name, last_name, age):
        """initiates Student

        Args:
            first_name (_str_): _represent name_
            last_name (_str_): _surname_
            age (_int_): _physical age_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get attributes of Student

        Returns:
            _dict_: _key value pairs of attributes_
        """
        return self.__dict__
