#!/usr/bin/python3
"""extending class student
"""


class Student:
    """create student
    """
    def __init__(self, first_name, last_name, age):
        """initiate student

        Args:
            first_name (_str_): _common name_
            last_name (_str_): _surname_
            age (_int_): _physical age_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get attributes

        Args:
            attrs (_list_, optional): _list of attributes_. Defaults to None.

        Returns:
            _dict_: _key value pairs of attributes_
        """
        if attrs is None:
            return self.__dict__
        dict_attr = set(self.__dict__)
        in_list = dict_attr.intersection(set(attrs))
        return {k: self.__dict__[k] for k in in_list}

    def reload_from_json(self, json):
        """set attributes

        Args:
            json (_json_): _key value pair of attributes_
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except Exception:
                pass
