#!/usr/bin/env python3

"""
Module for measuring the time taken by concurrent coroutines.
"""

import asyncio
import time

# Import the wait_n function from the 1-concurrent_coroutines module
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken by a specified number of concurrent
    coroutines.

    Args:
        n (int): The number of concurrent coroutines.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time taken by each coroutine in seconds.
    """
    # Record the start time
    start_time = time.time()

    # Run the wait_n coroutine using asyncio.run
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time

    # Calculate the average time taken per coroutine
    average_time = total_time / n

    # Return the average time taken per coroutine
    return average_time
