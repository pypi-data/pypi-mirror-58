"""Helper function for processing data from collections

This module provides functions to iterate over collections in specialized manner
not currently supported by `standard Python library`_.

.. _standard python library:
    https://docs.python.org/3.6/library/itertools.html
"""

from typing import Iterable, Iterator, List, Any


def batch(iterable: Iterable[Any], step: int) -> Iterator[List[Any]]:
    """Iterate over `iterable` and group items into batches size of `step`.

    This method is intended to be used in cases where you need to split a stream
    of data into batches of smaller size. Eg. When storing huge amount to database
    in batches of 1000 items. It will create an interatore that gives you a list
    of items in each iteration of size `step`. Last iteration will yield list of
    all remaining items.

    Example:
        >>> for i in batch(range(8), 3): print(i)
        [0, 1, 2]
        [3, 4, 5]
        [6, 7]
    """
    if not isinstance(step, int):
        raise TypeError(f'Step has to be an integer. {type(step)} given.')
    if step <= 0:
        raise IndexError(f'Step has to be larger than 0, {step} given.')
    items = []
    for i in iterable:
        items.append(i)
        if len(items) == step:
            yield items
            items = []
    if items:
        yield items
