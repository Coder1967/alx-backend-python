#!/usr/bin/env python3
"""
module for task number two
"""
import asyncio
from time import time
from typing import List
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather
    and return time taken
    """

    start_time: time = time()
    result: List[asyncio.Task] = await asyncio.gather(
                                *[async_comprehension() for num in range(4)])
    end_time: time = time()
    return end_time - start_time
