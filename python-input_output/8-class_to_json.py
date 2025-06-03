#!/usr/bin/python3
"""
Module: 8_class_to_json

Returns the dictionary description for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns a dictionary of all simple attributes for JSON serialization.

    Args:
        obj: The object to convert.

    Returns:
        dict: A dictionary of the object's attributes.
    """

    return obj.__dict__
