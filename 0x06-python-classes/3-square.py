#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines a squre with a private instance attribute called size"""

    def __init__(self, size=0):
        """instantializes a privated instance of a sqare"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size ** 2)
