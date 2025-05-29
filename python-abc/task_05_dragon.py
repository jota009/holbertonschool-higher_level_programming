#!/usr/bin/python3
"""
Module dragon.

Defines two mixins—SwimMixin and FlyMixin—and a Dragon class that
combines both abilities, plus an extra roar() method.
"""

class SwimMixin:
    """Mixin providing swim capability."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin providing fly capability."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """A mythical creature that can both swim and fly."""
    def roar(self):
        print("The dragon roars!")

if __name__ == "__main__":
    draco = Dragon()   # Dragon has swim, fly, and roar
    draco.swim()       # from SwimMixin
    draco.fly()        # from FlyMixin
    draco.roar()       # Dragon-specific
