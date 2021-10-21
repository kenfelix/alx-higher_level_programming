#!/usr/bin/python3
"""Base module.

Contains the base class.
"""


class Base:
    """The base of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id =__nb_objects
