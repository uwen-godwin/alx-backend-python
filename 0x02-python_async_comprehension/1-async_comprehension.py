#!/usr/bin/env python3
from typing import List
import asyncio
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
