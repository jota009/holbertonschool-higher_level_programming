#!/usr/bin/python3
"""
Module: 4_from_json_string

Converts a JSON string into a Python object.
"""


import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string

    Returns:
        The Python object representend by the JSON string.

    Example:
        >>> from_json_string('["a", 1, 2]')
        ['a', 1, 2]
        >>> from_json_string('{"name": "Josniel"}')
        {'name': 'Josniel'}
    """
    return json.loads(my_str)
