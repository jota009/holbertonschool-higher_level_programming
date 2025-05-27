#!/usr/bin/python3
"""Module that defines theh Basegeometry class."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Compute the area of the geometry.

        Raises:
            Exception: always, since this method must be
                overridden by subclasses.
        """
        raise Exception("area() is not implemented")
