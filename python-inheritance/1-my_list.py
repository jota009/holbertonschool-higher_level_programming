#!/usr/bin/python3
"""This module takes a MyList class that inherits
from list."""

class MyList(list):
    """Custom list that can print itself in sorted order."""

    def print_sorted(self):
        """Prints the elememnts of the list in ascending order."""
        print(sorted(self))
