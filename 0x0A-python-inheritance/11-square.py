#!/usr/bin/python3
"""Square module.
Contains a class Square that inherits from
BaseGeometry and some methods.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class that inherits from BaseGeometry."""

    def __init__(self, size):
        """Checks and sets the default attributes of Square class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Sets the behaviour of the str."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
