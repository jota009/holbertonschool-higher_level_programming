#!/usr/bin/python3
"""Module that defines is_same_class function."""


def is_same_class(obj, a_class):
    """Return True if ibj is exactly an instance of a_class.

    Args:
        obj: The object to test.
        a_class: The class to match againts.

    Returns:
        True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) is a_class
