#!/usr/bin/python3
"""
Module: 9-student

Defines a Student class with first_name, last_name, and age,
and a methos to get its dictionary representation.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary of the student's attribute.
        """
        return self.__dict__
