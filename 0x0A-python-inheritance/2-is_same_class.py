#!/usr/bin/python3
"""Same class module.

   contains only one function, is_same_class()
"""


def is_same_class(obj, a_class):
    """Checks of an object is exactly an instance of the specified class"""

    if type(obj) is a_class:
        return True
    else:
        return False
