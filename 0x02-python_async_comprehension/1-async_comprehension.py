#!/usr/bin/env python3

import asyncio
import random
from typing import List
async_generator = __import__("0-async_generator").async_generator

"""
Module containing an asynchronous comprehension function.

This module defines a single function, `async_comprehension`,
which generates a list of random numbers using an asynchronous generator.
"""


async def async_comprehension() -> List[float]:
    """
    An asynchronous comprehension function that generates a list of random
    numbers.

    This function uses an asynchronous generator to generate a list of random
    numbers.

    Returns:
        list[float]: A list of random numbers.
    """
    return [_ async for _ in async_generator()]
