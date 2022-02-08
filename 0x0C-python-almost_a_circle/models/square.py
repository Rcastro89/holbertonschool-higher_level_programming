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
        arg = ["id", "size", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, arg[i], value)
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary
        """
        return {"size": self.size, "x": self.x, "y": self.y, "id": self.id}
