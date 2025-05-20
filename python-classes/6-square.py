#!/usr/bin/python3
"""This module defines a Square class with size and position managements."""


class Square:
    """Represents a square with size, position, area,
    and print capabilities."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square.

            Args:
                size (int): Side length (default 0).
                position (tuple): (x, y) coordinates
                for printing offset (default 0, 0).

            Raises:
                TypeError: If size or position types are invalid.
                ValueError: If size < o or position values are negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square's size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The value to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            int: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (int): The value to assign.

        Raises:
            TypeError: If value is not a tuple.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the '#' character.

        The sqaure is offset by spaces according to position:
        - position[0] spaces before each line
        - position[1] blank lines before the square
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
