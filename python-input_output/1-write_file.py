#!/usr/bin/python3
"""
This module defines a single function, write_file,
which writes a UTF-8-encoded text string
to a file (creating or overwriting it)
and returns the numbers of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a UTF-8 string to a text file
    and returns the number of characters written.

    Args:
        filename (str): Path to (or name of) the file to write to.
                        If the file doesn't exist, it will be created.
                        If it does exist, its contents will be overwritten.
        text (str): The string to write into the file.
                    Can include new line characters.

    Returns:
        int: The total number of characters written into the file.

    Example:
        >>> write_file("test_output.txt", "Hello, Holberton\n
        This is a test.\n")
        29
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        num_chars = f.write(text)
        return num_chars
