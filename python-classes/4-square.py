#!/usr/bin/python3
"""This module defines a square with getter and setter."""


class Square:
    """Represents a square with managed size access."""

    def __init__(self, size=0):
        """Initializes a new Square object.

        Args:
            size (int): The size of one side of the square. Defaults to 0.

        This calls the setter methos to validate the input.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square.

        Returns:
            int: Area computed as size squared.
        """
        return self.__size ** 2
