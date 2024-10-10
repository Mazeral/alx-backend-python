#!/usr/bin/env python3

"""
Module for converting key-value pairs.

This module provides a function for converting a key-value
pair into a tuple, where the value is squared.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the key and the squared value.

    Args:
        k (str): The key of the key-value pair.
        v (Union[int, float]): The value of the key-value pair,
        which can be an integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing the key
        and the squared value.

    Examples:
        >>> to_kv("x", 2)
        ('x', 4)
        >>> to_kv("y", 3.0)
        ('y', 9.0)
    """
    return (k, v**2)
