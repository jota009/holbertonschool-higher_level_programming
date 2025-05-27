#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited
    (directly or inderectly) from a_class; otherwise False.

    Args:
        obj: The object to test.
        a_class: The class to match againts.

    Returns:
        True if obj.__class__ is a subclass of a_class but not exactly a_class.
    """
    cls = type(obj)
    return issubclass(cls, a_class) and cls is not a_class
