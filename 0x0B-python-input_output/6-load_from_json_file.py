#!/usr/bin/python3
"""Create object from a JSON file.

Contains only one function, load_from_json_file().
"""
import json


def load_from_json_file(filename):
    """
        Creates an Object from a JSON file.
    """
    with open(filename, 'r') as f:
        json.loads(f.read(filename))
