#!/usr/bin/python3
"""
Module: 5_save_to_json_file

Saves a Python object to a text file in JSON format.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file as JSON.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The file to write to.

    Returns:
        None.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
