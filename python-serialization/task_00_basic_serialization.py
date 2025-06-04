#!/usr/bin/python3
"""
Module: task_00_basic_serialization

Provides basic functions to serialize a Python dictionary to a JSON file
and to  deserialize a JSON file back into a Python dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the JSON file to write to.

    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it back into a Python dictionary

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The dictionary reconstructed from the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)

