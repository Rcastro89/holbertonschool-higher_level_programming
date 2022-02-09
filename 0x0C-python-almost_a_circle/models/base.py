#!/usr/bin/python3
"""module base"""


import json
import csv


class Base():
    """class main base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """jason"""
        if not list_dictionaries or list_dictionaries == [None]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save"""
        save = []
        if list_objs is not None and len(list_objs) > 0:
            save = [(i.to_dictionary()) for i in list_objs]
        with open(cls.__name__ + ".json", "w") as my_file:
            my_file.write(cls.to_json_string(save))

    @staticmethod
    def from_json_string(json_string):
        """from json"""
        if not json_string or json_string == [None]:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == 'Rectangle':
            r = cls(1, 1)
        if cls.__name__ == 'Square':
            r = cls(1)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """load from file"""
        try:
            with open(cls.__name__ + ".json", "r") as my_file:
                return ([(cls.create(**i))
                        for i in Base.from_json_string(my_file.read())])
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file """
        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file """
        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    res_dict[k] = int(v)
                res.append(cls.create(**res_dict))
        return res
