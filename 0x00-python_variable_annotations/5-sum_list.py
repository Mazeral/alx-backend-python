#!/usr/bin/env python3

"""
Module for list operations.

This module provides a function for calculating the sum of a list of integers.
"""

from typing import List


def sum_list(input_list: List[int]) -> float:
    """
    Returns the sum of a list of integers as a floating point number.

    Args:
        input_list (List[int]): A list of integers to calculate the sum of.

    Returns:
        float: The sum of the integers in the input list.

    Examples:
        >>> sum_list([1, 2, 3, 4, 5])
        15.0
    """
    sum_value: float = 0  # Initialize sum variable
    for i in range(len(input_list)):  # Iterate over the input list
        sum_value += input_list[i]  # Add each element to the sum
    return sum_value  # Return the calculated sum
