#!/usr/bin/python3
"""Save object to file module.

Containd only one function, save_to_json_file().
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    """
    with open(filename, 'w') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
