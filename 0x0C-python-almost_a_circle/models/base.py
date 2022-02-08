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
        if list_objs is not None and len(list_objs) > 0:
            save = [(i.to_dictionary()) for i in list_objs]
            with open(cls.__name__ + ".json", "w") as my_file:
                my_file.write(Base.to_json_string(save))

    @staticmethod
    def from_json_string(json_string):
        """from json"""
        if not json_string or json_string == [None]:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        r = cls(1, 1)
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
        """csv"""
        save = [(i.to_dictionary()) for i in list_objs]
        with open(cls.__name__ + ".csv", "w") as my_file:
            writer = csv.writer(my_file)
            for i in save:
                for key, value in i.items():
                    writer.writerow([key, value])

    @classmethod
    def load_from_file_csv(cls):
        """Load csv"""
        if cls.__name__ == "Rectangle":
            var_ctr = 5
        elif cls.__name__ == "Square":
            var_ctr = 4
        else:
            var_ctr = 1
        try:
            with open(cls.__name__ + ".csv", mode='r') as f:
                reader = csv.reader(f)
                i = 1
                list_dir = []
                dict_from_csv = {}
                for rows in reader:
                    if i <= var_ctr:
                        dict_from_csv[rows[0]] = int(rows[1])
                        i += 1
                    else:
                        list_dir.append(dict_from_csv.copy())
                        dict_from_csv[rows[0]] = int(rows[1])
                        i = 1
                list_dir.append(dict_from_csv.copy())
                return [cls.create(**i) for i in list_dir]
        except Exception:
            return []
