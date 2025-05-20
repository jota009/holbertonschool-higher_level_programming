#!/usr/bin/python3
"""This module defines a Square class wi, area, and print methods."""


class Square:
    """Represents a square with size validation,
    area computation and printing."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): The size of one side of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square.

        Returns:
            int: The size of the square's side.
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
        """Returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
