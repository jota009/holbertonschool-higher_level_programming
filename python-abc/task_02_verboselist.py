#!/usr/bin/python3
"""
Module verbose_list.

Defines VerboseList, a subclass of list that logs every append, extend, remove, and pop.
"""

class VerboseList(list):
    """List subclass that prints notifications on modifications."""

    def append(self, item):
        """Add item and notify."""
        super().append(item)                  # perform the real append
        print(f"Added {item!r} to the list.")  # notification

    def extend(self, iterable):
        """Extend with iterable and notify count."""
        count = len(iterable)
        super().extend(iterable)              # perform the real extend
        print(f"Extended the list with {count} items.")  # notification

    def remove(self, item):
        """Notify then remove item."""
        print(f"Removed {item!r} from the list.")
        super().remove(item)                  # perform the real remove

    def pop(self, index=-1):
        """Notify then pop at index (default last)."""
        item = super().pop(index)             # perform the real pop
        print(f"Popped {item!r} from the list.")
        return item                           # return the popped value


if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)            # Added 4
    vl.extend([5, 6])       # Extended with 2 items
    vl.remove(2)            # Removed 2
    vl.pop()                # Popped 6
    vl.pop(0)               # Popped 1
    print(vl)               # remaining contents
