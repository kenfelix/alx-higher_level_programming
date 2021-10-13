#!/usr/bin/python3
"""MyInt module.

Contains only one class, MyInt() and some methods.
"""


class MyInt(int):
    """Defines the MyInt Class"""

    def __eq__(self, other):
        """Sets the == behaviour."""
        return int(self) != other

    def __ne__(self, other):
        """Sets the != behaviour."""
        return int(self) == other
