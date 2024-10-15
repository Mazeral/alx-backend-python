#!/usr/bin/env python3

"""
Module to measure the runtime of async_comprehension coroutine.

This module imports the async_comprehension coroutine from another module and
defines a new coroutine, measure_runtime, to measure the total runtime of
async_comprehension when executed four times concurrently.
"""

import time
import asyncio
from typing import Awaitable

# Import the async_comprehension coroutine from another module
async_comprehension: Awaitable = __import__("1-async_comprehension")\
        .async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of async_comprehension coroutine when executed
    four times concurrently.

    This coroutine uses asyncio.gather to run four instances of
    async_comprehension concurrently and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    # Record the start time
    start_time: float = time.time()

    # Run four instances of async_comprehension concurrently
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    # Record the end time
    end_time: float = time.time()

    # Calculate and return the total runtime
    return end_time - start_time
