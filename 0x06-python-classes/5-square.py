#!/usr/bin/python3
"""Module that create a class called square."""


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
        else:
            self.__size = size

    def area(self):
        """calculate area of square"""
        area = self.__size * self.__size
        return (area)

    @property
    def size(self):
        """method getter, get value of size"""
        return self.__size

    @size.setter
    def size(self, value=0):
        """method setter, set value of size"""

        if(type(value) != int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """method for print square whit #"""

        if (self.size != 0):
            x = self.size
            while (x > 0):
                y = self.size
                while (y > 0):
                    print("#", end="")
                    y -= 1
                print()
                x -= 1
            print()
        else:
            print()
