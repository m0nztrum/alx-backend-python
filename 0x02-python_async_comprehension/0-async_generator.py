#!/usr/bin/env python3
"""Task 0: Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10x, each time
    asynchronously wait 1sec then yield a random
    number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
