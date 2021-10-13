#!/usr/bin/python3
"""Square module.
Contains a class Square that inherits from
BaseGeometry and some methods.
"""
BaseGeometry = __import__('9-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Defines the Square class that inherits from BaseGeometry."""

    def __init__(self, size):
        """Checks and sets the default attributes of Square class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
