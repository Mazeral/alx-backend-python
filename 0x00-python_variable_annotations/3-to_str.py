#!/usr/bin/env python3

"""
Module for type conversions.

This module provides a simple function for converting floats to strings.
"""


def to_str(n: float) -> str:
    """
    Returns the string representation of an float.

    Args:
        n (float): The float to convert to a string.

    Returns:
        str: The string representation of n.

    Examples:
        >>> to_str(123)
        '123'
        >>> to_str(-456)
        '-456'
    """
    return str(n)
