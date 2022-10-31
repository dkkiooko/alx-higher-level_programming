#!/usr/bin/python3
"""base
"""
import json
import csv


class Base:
    """base for other shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.loads(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([item.to_dictionary()
                                            for item in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        res = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                res.append(cls.create(**item))
            else:
                res.append(item)
        return res

    @classmethod
    def load_from_file_csv(cls):
        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    res_dict[k] = int(v)
                res.append(cls.create(**res_dict))
        return res
