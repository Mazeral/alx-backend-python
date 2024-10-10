#!/usr/bin/env python3

"""
Module for creating multiplier functions.

This module provides a function for creating a multiplier
function that takes a float argument and returns the product
of the argument and a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float argument and
        returns the product of the argument and the multiplier.

    Examples:
        >>> double = make_multiplier(2.0)
        >>> triple = make_multiplier(3.0)
        >>> print(double(5.0))  # Output: 10.0
        >>> print(triple(5.0))  # Output: 15.0
    """
    def multiply(x: float) -> float:
        """
        Multiplies a float by a given multiplier.

        Args:
            x (float): The number to multiply.

        Returns:
            float: The product of x and the multiplier.
        """
        return x * multiplier
    return multiply
