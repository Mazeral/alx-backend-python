#!/usr/bin/env python3

"""
Module containing an asynchronous generator function.

This module defines a single function, `async_generator`,
which generates a sequence
of random numbers asynchronously.
"""

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator function that yields a sequence
    of random numbers.

    This function generates 10 random numbers between 0 and 10,
    with a 1-second delay between each number.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        # Pause execution for 1 second to simulate asynchronous behavior
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.uniform(0, 10)
