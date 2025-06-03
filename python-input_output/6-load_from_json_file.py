#!/usr/bin/python3
"""
Module: 6_loas_from_json_file

Loads a Python object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The Python object created from the file's JSON data.

    Example:
        >>> # If 'data.json' contains: {"a": 1, "b": 2}
        >>> load_from_json_file("data.json")
        {'a': 1, 'b': 2}
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
