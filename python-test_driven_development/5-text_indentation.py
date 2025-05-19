#!/usr/bin/python3
"""
    Defines a function that prints text with 2 new lines.
    After '.', '?', and ':'.
"""


def text_indentation(text):
    """Prints text with two new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip())
