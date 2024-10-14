#!/usr/bin/env python3

"""
Module for asynchronous random delay functionality.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time period.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The actual delay time in seconds.
    """
    # Generate a random wait time between 0 and max_delay seconds
    wait_time = random.uniform(0, max_delay)

    # Asynchronously wait for the generated time period
    await asyncio.sleep(wait_time)

    # Return the actual delay time
    return wait_time
