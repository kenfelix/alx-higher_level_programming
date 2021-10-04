#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """A Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieves the width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setd the height value"""
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
