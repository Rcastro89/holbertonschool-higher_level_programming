#!/usr/bin/python3
"""Module for print
class empty
"""


class Square():
    """class empty"""
    pass

    def __init__(self, size=0):
        """generate atribute private
        self: """

        if(type(size) != int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate area of square"""
        area = self.__size * self.__size
        return (area)
