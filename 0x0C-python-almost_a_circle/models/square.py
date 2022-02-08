#!/usr/bin/python3
"""square"""


from turtle import width
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square what inheredith Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """method Init constructor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str functions"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """method getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        

    def update(self, *args, **kwargs):
        """update"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "y":
                    self.y = value
                if key == "x":
                    self.x = value
                if key == "size":
                    self.__size = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """dictionary"""
        attr = ["id", "x", "size", "y"]
        dir = {}
        for key in attr:
            dir[key] = getattr(self, key)
        return dir
