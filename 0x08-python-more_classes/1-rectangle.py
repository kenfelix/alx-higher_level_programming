#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """A Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, width_value):
        """sets the width value"""
        self.__width = width_value

        if not isinstance(width_value, int):
            raise TypeError("width must be an integer")
        elif width_value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieves the width"""
        return self.__height

    @height.setter
    def height(self, height_value):
        """setd the height value"""
        self.__height = height_value

        if not isinstance(height_value, int):
            raise TypeError("height must be an integer")
        elif height_value < 0:
            raise ValueError("height must be >= 0")
