#!/usr/bin/python3
"""Module that defines a subclass of Rectangle(from 9-rectangle.py)."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, defined by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The lenght of the square's side.

        Requirements:
        - Validate 'size' as a positive integer uing integer_validation()
        - Store it as a private attribute (no getter/setter)
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Compute and return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the print description: [Square] width/height."""
        return "[Square] {}/{}".format(self.__size, self.__size)
