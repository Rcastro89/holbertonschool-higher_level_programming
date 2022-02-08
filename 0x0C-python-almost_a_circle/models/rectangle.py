#!/usr/bin/python3
"""module rectangle"""


from models.base import Base


class Rectangle(Base):
    """class main base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """method getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """method getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """method getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """method getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectagle in screen"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "y":
                    self.__y = value
                if key == "x":
                    self.__x = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """dictionary"""
        attr = ["x", "y", "id", "height", "width"]
        dir = {}
        for key in attr:
            dir[key] = getattr(self, key)
        return dir
