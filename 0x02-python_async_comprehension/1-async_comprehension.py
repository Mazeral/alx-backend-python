#!/usr/bin/env python3

"""
Module containing an asynchronous comprehension function.

This module defines a single function, `async_comprehension`,
which generates a list of random numbers using an asynchronous generator.
"""

import asyncio
import random
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> list[float]:
    """
    An asynchronous comprehension function that generates a list of random
    numbers.

    This function uses an asynchronous generator to generate a list of random
    numbers.

    Returns:
        list[float]: A list of random numbers.
    """
    return [x async for x in async_generator()]
