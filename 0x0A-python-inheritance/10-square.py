#!/usr/bin/python3
"""file Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherated"""

    def __init__(self, size):
        """init main"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
