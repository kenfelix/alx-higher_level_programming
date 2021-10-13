#!/usr/bin/python3
"""Read_file module.

Contains the only one function, read_file().
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r') as f:
        print(f.read(), end='')
