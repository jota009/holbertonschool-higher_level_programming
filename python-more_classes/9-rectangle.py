#!/usr/bin/python3
"""This module defines a Rectangle class with factory methods
and comparison."""


class Rectangle:
    """Represents rectangle by its width and height
    with instance counting, customizable print sybmol, comparison,
    and square factory."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
           width (int): The width of the rectangle (default 0)
           height (int): The height of the rectangle (default 0)

        Raises:
            TypeEror: if width is not an integer.
            ValueError: if width is < 0
        """
        Rectangle.number_of_instances += 1
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
        (2*(w+h), or 0 if either is 0)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with 'print_symbol', or empty string."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        lines = []
        for _ in range(self.__height):
            lines.append(symbol * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """Return an eval()-able string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a farewell message when the instance is about
        to be destroyed."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area.

        Args:
            rect_1: (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of Rectangle

        Returns:
            Rectangle: rect_1 if its area >= rect_2's area, else rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new Rectangle instance with width == height
        == size.

        Args:
            size (int): The size of the square's side (default 0).

        Returns:
            Rectangle: new rectangle where width and height both equal size.
        """
        return cls(size, size)
