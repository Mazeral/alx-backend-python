README
================

Table of Contents
-----------------

1. [Async Generator](#async-generator)
2. [Async Comprehensions](#async-comprehensions)
3. [Run Time for Four Parallel Comprehensions](#run-time-for-four-parallel-comprehensions)

### Async Generator

#### Description

This task involves creating a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10.

#### Code

```python
# 0-async_generator.py
import asyncio
import random

async def async_generator():
    """
    A coroutine that generates 10 random numbers asynchronously.
    
    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### Async Comprehensions

#### Description

This task involves creating a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

#### Code

```python
# 1-async_comprehension.py
import asyncio
from . import async_generator

async def async_comprehension():
    """
    A coroutine that collects 10 random numbers using an async comprehension.
    
    Returns:
        list[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator.async_generator()]
```

### Run Time for Four Parallel Comprehensions

#### Description

This task involves creating a coroutine called `measure_runtime` that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.

#### Code

```python
# 2-measure_runtime.py
import asyncio
from . import async_comprehension
import time

async def measure_runtime():
    """
    A coroutine that measures the total runtime of four parallel comprehensions.
    
    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension.async_comprehension(),
        async_comprehension.async_comprehension(),
        async_comprehension.async_comprehension(),
        async_comprehension.async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
```

Note: The total runtime is roughly 10 seconds because each comprehension takes approximately 10 seconds to complete, and they are executed in parallel. The total runtime is not exactly 10 seconds due to the overhead of creating and managing the coroutines.

---
Author: Mohammad Omar Siddiq Ahmad
