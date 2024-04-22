#!/usr/bin/env python3
"""Task 1: Let's execute multiple coroutines
    at the same time with async
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    wait_times = await asyncio.gather(
        *list(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
