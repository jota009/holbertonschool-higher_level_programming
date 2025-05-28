#!/usr/bin/python3
"""
Defines an abstract Animal base class and two concretes subclasses:
Dog and Cat, each implementing sound() method.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.
    Subclasses must implement the sound() method.
    """
    @abstractmethod
    def sound(self):
        """
        Produce the characteristic sound of the animal.
        Must return a string, e.g "Bark" or "Meow".
        """
        pass


class Dog(Animal):
    """
    Concrete Animal subclass representing a dog.
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Concrete Animal subclass representing a cat.
    """

    def sound(self):
        return "Meow"
