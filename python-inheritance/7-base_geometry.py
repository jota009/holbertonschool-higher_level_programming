#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""
import sys

class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Compute the area of the geometry.

        Raises:
            Exception: always, since this method must be
                overridden by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a given value is a positive integer.

        Args:
            name(str): Identifier used in error messages.
            value(any): The value to validate.

        Raises:
            TypeError: if 'value' is not an integer.
            ValueError: if 'value' is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
