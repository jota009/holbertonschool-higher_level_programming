#!/usr/bin/python3
"""This module defines a Rectangle class with
eval-able repr."""


class Rectangle:
    """Represents rectangle with width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
           width (int): The width of the rectangle (default 0)
           height (int): The height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle.

        Returns:
            int: The rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width validation.

        Args:
            value (int): The new width to assign.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle.

        Returns:
            int: The rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        If either width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation '#'.

        For a rectangle of width w and height h, produces h lines
        each containing w '#' characters. If either dimension is 0,
        returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """Return an eval()-able string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"
