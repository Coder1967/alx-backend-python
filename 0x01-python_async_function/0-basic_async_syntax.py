#!/usr/bin/env python3
"""
module of task 1
"""
import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes in an integer argument (max_delay, with a default value of 10) named
    'wait_random' that waits for a random delay between 0 and 'max_delay'
    (included and float value) seconds and eventually returns it.
    """

    rand_num: float = random() * 10
    await asyncio.sleep(rand_num)
    return rand_num
