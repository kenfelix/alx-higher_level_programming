#!/usr/bin/python3
"""Append Write module.

Contains only one function, append_write().
"""


def append_write(filename="", text=""):
    """
       Appends a string at the end of a text file(UTF8)
       and returns the number of characters added.
    """
    with open(filename, 'a') as f:
        return f.write(text)
