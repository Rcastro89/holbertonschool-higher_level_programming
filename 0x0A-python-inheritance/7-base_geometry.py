#!/usr/bin/python3
"""module bass"""


class BaseGeometry():
    """Base Geometryc"""

    def area(self):
        """Method define area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method Validate value int"""

        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
