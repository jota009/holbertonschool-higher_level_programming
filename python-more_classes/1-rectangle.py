#!/usr/bin/python3
"""This module defines a rectangle with private
width and height attribute."""


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
        """Sets the height of the rectangle.

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
