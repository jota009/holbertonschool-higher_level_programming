#!/usr/bin/python3
"""
Module: 2_append_write

Appends a string to a text file (UTF-8) and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append 'text' to the end of 'filename'.
    Returnnumber of characters added.

    If the file doesn't exist, create it.

    Args:
        filename (str): The file to append to.
        text (str): The string to add.

    Returns:
        int: Characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
