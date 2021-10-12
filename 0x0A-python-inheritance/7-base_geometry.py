#!/usr/bin/python3
"""BaseGeometry Module (based on 6-base_geometry.py).

Contains a class, BaseGeometry() and some methods.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """raises an Exception with the message."""
        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
