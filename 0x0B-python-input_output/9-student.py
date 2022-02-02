#!/usr/bin/python3
"""class to json"""


class Student():
    """class"""

    def __init__(self, first_name, last_name, age):
        """method init main"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return class"""
        return self.__dict__
