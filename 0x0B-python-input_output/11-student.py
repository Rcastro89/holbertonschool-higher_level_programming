#!/usr/bin/python3
"""class to json"""


class Student():
    """class"""

    def __init__(self, first_name, last_name, age):
        """method init main"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """tojason"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__:
                dic[i] = self.__dict__[i]
        return dic

    def reload_from_json(self, json):
        """reload"""
        myList = json.items()
        myList = list(myList)
        dic = {}
        for i in myList:
            if i[0] in self.__dict__:
                self.__dict__[i[0]] = i[1]
        return self.__dict__
