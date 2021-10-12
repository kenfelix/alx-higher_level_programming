#!/usr/bin/python3
"""Same class module.

Contains only one function, is_same_class().
"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or a class that inherited from, the specified class """

    return (isinstance(obj, a_class))
