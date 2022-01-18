#!/usr/bin/python3
"""Module that create a class called square."""


class Square():
    """class empty"""

    def __init__(self, size=0, position=(0, 0)):
        """generate atribute private
        self: """
        self.size = size
        self.position = position

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
        p = self.__position
        if (self.size != 0):
            for i in range(p[0]):
                print(" ", end='')
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """method getter, get value of size"""
        return self.__position

    @position.setter
    def position(self, value):
        """method setter, set value of size"""
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
