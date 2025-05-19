#!/usr/bin/python3
"""Defines a function that prints text with 2 new lines.
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

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    for line in result.split("\n"):
        stripped = line.strip()
        if stripped:
            print(stripped)
