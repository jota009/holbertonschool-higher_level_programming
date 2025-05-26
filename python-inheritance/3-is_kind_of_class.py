#!/usr/bin/python3
"""This module defines is_kind_of_class function."""

def is_kind_of_class(obj, a_class):
    """Returns True if the obj is an instance of
    or if obj is an instance of inherited class.

    Args:
        obj: The object to test.
        a_class: The class to match againts.

    Returns:
       True if obj is an instance of a_class or its subclass,
       otherwise False.
    """
    return isinstance(obj, a_class)
