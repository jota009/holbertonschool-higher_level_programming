#!/usr/bin/python3
"""
Module: task_01_pickle

Deinfes a CustomObject class than cna be pickeled(serialized)
and unpickeled (deserialiazed)
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject.

        Args:
            name (str): The name of the person.
            age (int): Their age.
            is_student (bool): If they're a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attribute in the specified format.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is student:", self.is_student)

    def serialize(self, filename):
        """
        Serialize (pickles) this object to the given file.

        Args:
            filename (str): File to save to.

        Returns:
            None if an error occurs, othersise True or None.
        """
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes (unpickles) an object from the given file.

        Args:
            filename (str): File to load from.

        Returns:
            CustomObject instance or None if error.
        """
        try:
            with open(filename, mode="rb") as f:
                return pickle.load(f)
        except Exception:
            return None
