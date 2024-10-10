#!/usr/bin/env python3

"""
Module for mathematical operations.

This module provides a simple function for calculating the floor of a number.
"""

import math


def floor(n: float) -> int:
    """
    Returns the largest integer not greater than the given number.

    Args:
        n (float): The number to calculate the floor of.

    Returns:
        int: The floor of n.

    Examples:
        >>> floor(3.7)
        3
        >>> floor(-3.7)
        -4
    """
    return math.floor(n)
