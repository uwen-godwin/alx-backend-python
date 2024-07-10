#!/usr/bin/env python3
"""
Module which handles a coroutine generator function that returns a float.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine function that generates a sequence of 10 random float numbers between 0 and 10.
    
    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
