#!/usr/bin/python3
"""
This module defines a single function, read_file
which read a UTF-8 encoded text file and prints its contents to stdout, exactly as it appears in the file.
No erros handling for missing files or permission issues is required.
"""
def read_file(filename=""):
    """
    Read a UTF-8 text file and prints its contents to stdout.

    Args:
        filename (str): Path to the UTF-8-encoded text file.

    Returns:
        None

    Example:
        >>> read_file("example.txt")
        (prints the entire contents of example.txt to stdout.)
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        contents = f.read()
        print(contents, end="")
