#!/usr/bin/env python3

"""
Module for list operations.

This module provides a function for calculating the sum of a list containing
integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats as a floating
    point number.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and
        floats to calculate the sum of.

    Returns:
        float: The sum of the integers and floats in the input list.

    Examples:
        >>> sum_mixed_list([1, 2.0, 3, 4.0])
        10.0
        >>> sum_mixed_list([1.0, 2, 3.0, 4])
        10.0
    """
    return sum(mxd_lst)
