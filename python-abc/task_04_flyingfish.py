#!/usr/bin/python3
"""
Module flying_fish.

Demonstrates multiple inheritance via Fish, Bird, and FlyingFish.
"""

class Fish:
    """Base class for aquatic creatures."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Base class for aerial creatures."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A creature that can both swim and fly."""

    def fly(self):
        """Override Bird.fly."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override Fish.swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override both parents’ habitat."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    ff = FlyingFish()
    ff.swim()        # -> The flying fish is swimming!
    ff.fly()         # -> The flying fish is soaring!
    ff.habitat()     # -> The flying fish lives both in water and the sky!

    # Inspect Method Resolution Order
    print("\nMRO:", [cls.__name__ for cls in FlyingFish.mro()])
