#!/usr/bin/env python3

"""
Module for calculating element lengths.

This module provides a function for calculating the lengths
of elements in an iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
        contains a sequence and its length.

    Examples:
        >>> element_length([['a', 'b', 'c'], ['d', 'e'], ['f']])
        [(['a', 'b', 'c'], 3), (['d', 'e'], 2), (['f'], 1)]
        >>> element_length([('a', 'b', 'c'), ('d', 'e'), ('f')])
        [(('a', 'b', 'c'), 3), (('d', 'e'), 2), (('f',), 1)]
    """
    return [(i, len(i)) for i in lst]
