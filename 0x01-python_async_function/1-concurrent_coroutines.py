#!/usr/bin/env python3

"""
Module for asynchronous random delay functionality.
"""

import asyncio
import importlib
import random
from typing import List

# Import the wait_random function from the 0-basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Asynchronously waits for a specified number of random time periods.

    Args:
        n (int): The number of random time periods to wait for.
        max_delay (int): The maximum delay in seconds.

    Returns:
        list[float]: A list of the actual delay times in seconds,
        sorted in ascending order.
    """
    # Generate a list of n random wait times using asyncio.gather
    # The * is used to unpack the list, so asyncio.gather treats each
    # item as a separate task
    randoms = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    # Return the sorted list of random wait times
    return sorted(randoms)
