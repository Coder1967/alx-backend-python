#!/usr/bin/env python3
"""
module for task number zero
"""
import asyncio
from random import random
from typing import List


async def async_generator() -> List[float]:
    """
    coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10
