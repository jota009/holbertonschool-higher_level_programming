#!/usr/bin/python3
"""Module that defines Rectangle with custom string representation."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle shape, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): the rectangle's width.
            height (int): the rectangle's height.

        Both must be validated as positive integers by
        BaseGeometry.integer_validator(), then stored
        as private attributes.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Compute and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the "print" description: [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
