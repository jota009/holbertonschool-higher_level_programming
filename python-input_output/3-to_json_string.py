#!/usr/bin/python3
"""
Module: 3_to_json_string.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of my_obj.

    Args:
        my_obj: The Python object to convert (eg. dict, list, string, etc.)

    Returns:
        str: JSON string representation of my_obj.

    Example:
        >>> to_json_string({"a": 1, "b": 2})
        '{"a": 1, "b": 2}'
    """
    return json.dumps(my_obj)
