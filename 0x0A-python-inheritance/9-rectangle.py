#!/usr/bin/python3
"""file rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherated"""

    def __init__(self, width, height):
        """init main"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """calculate area of rectangle"""

        area = self.__width * self.__height
        return (area)

    def __str__(self):
        """return area print str"""
        cad = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return (cad)
