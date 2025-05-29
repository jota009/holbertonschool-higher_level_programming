#!/usr/bin/python3
"""
Module shapes.

Defines an abstract Shape base class and two concrete subclasses,
Circle and Rectangle, each implementing area() and perimeter().
Also provides a duck-typed helper shape_info().
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.
    Defines the interface: area() and perimeter() must be implemented.
    """
    @abstractmethod
    def area(self):
        """
        Compute and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete Shape: circle defined by its radius.
    """

    def __init__(self, radius):
        """
        Initialize a new Circle.

        Args:
            radius (int or float): the circle's radius
        """
        self.radius = radius

    def area(self):
        """
        Return pi times radius to the square root
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the circumference: 2 x pi x radius."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete Shape: a rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int or float): the rectangle's width
            heigh (int or float): the rectangle's height
        """
        self.width = width
        self.height = height

    def area(self):
        """Return width x height."""
        return self.width * self.height

    def perimeter(self):
        """Return 2 x (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any duck-typed Shape.

    Args:
        shape: and object implementing .area() and .perimeter()
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    c = Circle(3)
    r = Rectangle(4, 5)
    print("Circle(3):")
    shape_info(c)
    print("---")
    print("Rectangle(4, 5):")
    shape_info(r)
