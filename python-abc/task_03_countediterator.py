#!/usr/bin/python3
"""
Module counted_iterator.

Defines CountedIterator, an iterator wrapper that counts how many items have been returned.
"""

class CountedIterator:
    """Iterator that keeps track of how many elements have been iterated."""

    def __init__(self, iterable):
        """
        Initialize with any iterable.

        Args:
            iterable: any Python iterable (list, tuple, generator, etc.)
        """
        self._iter = iter(iterable)  # underlying iterator
        self._count = 0              # number of items fetched so far

    def __iter__(self):
        """Return self as the iterator object."""
        return self

    def __next__(self):
        """
        Fetch the next item, increment the counter, and return it.

        Raises:
            StopIteration: when the underlying iterator is exhausted.
        """
        item = next(self._iter)  # may raise StopIteration
        self._count += 1
        return item

    def get_count(self):
        """
        Return the number of items fetched so far.

        Returns:
            int: how many times __next__ has been successfully called.
        """
        return self._count


if __name__ == "__main__":
    data = [10, 20, 30]
    it = CountedIterator(data)

    for val in it:
        print(val, "count =", it.get_count())
    # After loop, get_count() should equal len(data)
    print("Total items iterated:", it.get_count())
