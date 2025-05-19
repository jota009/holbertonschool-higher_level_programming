#!/usr/bin/python3
"""This module defines a square with a private size attribute."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new square.
        Args:
            size: The size of the square (no type/value validation).
        """
        self.__size = size
