#!/usr/bin/env python3
"""
Module for waiting for multiple random time periods.
"""

import asyncio
from typing import List

# Import the task_wait_random function from the 3-tasks module
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for `n` random amounts of time up to `max_delay` seconds.

    Args:
        n (int): The number of random time periods to wait for.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of the wait times, sorted in ascending order.
    """
    # Create a list of tasks that wait for random time periods
    # using asyncio.gather and a lambda function to map task_wait_random
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    # Sort the list of wait times in ascending order
    sorted_wait_times = sorted(wait_times)

    # Return the sorted list of wait times
    return sorted_wait_times
