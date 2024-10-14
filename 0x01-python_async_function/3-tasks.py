#!/usr/bin/env python3

"""
Module for creating tasks that wait for a random time period.
"""

import asyncio
# Import the wait_random function from the 0-basic_async_syntax module
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a task that waits for a random time period.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that waits for a random time period.
    """
    # Create a task that waits for a random time period using asyncio.Task
    # Note: asyncio.Task is deprecated since Python 3.7,
    # use asyncio.create_task instead
    return asyncio.create_task(wait_random(max_delay))
