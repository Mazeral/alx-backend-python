#!/usr/bin/env python3

"""
Module for string concatenation.

This module provides a simple function for concatenating two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Returns the concatenation of two strings.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenation of str1 and str2.

    Examples:
        >>> concat("Hello, ", "World!")
        'Hello, World!'
    """
    return str1 + str2
