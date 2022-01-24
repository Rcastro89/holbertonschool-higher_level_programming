#!/usr/bin/python3
"""Module for print class empty"""


class Rectangle():
    """class empty"""

    def __init__(self, width=0, height=0):
        """generate atribute private
        self: """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method getter, get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """method setter, set value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """method getter, get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method setter, set value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate area of rectangle"""
        area = self.__width * self.__height
        return (area)

    def perimeter(self):
        """calculate perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        per = (self.__width * 2) + (self.__height * 2)
        return (per)

    def __str__(self):
        """return area print str"""
        cad = ""
        if self.__height == 0 or self.__width == 0:
            return (cad)
        for i in range(self.__height):
            for k in range(self.__width):
                cad = cad + "#"
            cad = cad + "\n"
        cad = cad[:-1]
        return (cad)
