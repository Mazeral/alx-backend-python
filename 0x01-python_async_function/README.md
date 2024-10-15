README
======

Table of Contents
-----------------

1. [0-basic_async_syntax.py](#0-basic_async_syntaxpy)
2. [1-concurrent_coroutines.py](#1-concurrent_coroutinespy)
3. [2-measure_runtime.py](#2-measure_runtimepy)
4. [3-tasks.py](#3-tasks)
5. [4-tasks.py](#4-tasks)

### 0-basic_async_syntax.py

This file contains an asynchronous coroutine `wait_random` that waits for a random delay between 0 and `max_delay` (inclusive) seconds and returns the delay.

#### Usage

```python
import asyncio
from 0_basic_async_syntax import wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

### 1-concurrent_coroutines.py

This file contains an asynchronous coroutine `wait_n` that spawns `wait_random` `n` times with the specified `max_delay` and returns the list of all delays in ascending order.

#### Usage

```python
import asyncio
from 1_concurrent_coroutines import wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

### 2-measure_runtime.py

This file contains a function `measure_time` that measures the total execution time for `wait_n(n, max_delay)` and returns the average execution time per task.

#### Usage

```python
from 2_measure_runtime import measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

### 3-tasks.py

This file contains a function `task_wait_random` that returns an `asyncio.Task` that waits for a random delay between 0 and `max_delay` seconds.

#### Usage

```python
import asyncio
from 3_tasks import task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### 4-tasks.py

This file contains a function `task_wait_n` that spawns `task_wait_random` `n` times with the specified `max_delay` and returns the list of all delays.

#### Usage

```python
import asyncio
from 4_tasks import task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```

Implementation
-------------

### 0-basic_async_syntax.py

```python
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
```

### 1-concurrent_coroutines.py

```python
import asyncio
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> list:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
```

### 2-measure_runtime.py

```python
import time
from 1_concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
```

### 3-tasks.py

```python
import asyncio
from 0_basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
```

### 4-tasks.py

```python
import asyncio
from 3_tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> list:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
```

---
Author: Mohammad Omar Siddiq Ahmad
