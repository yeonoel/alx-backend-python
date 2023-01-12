#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async."""


import asyncio
from typing import List
from array import array
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values). The
        list of the delays should be in ascending
        order without using sort()."""
    arr, desc = [], []
    for i in range(n):
        desc.append(wait_random(max_delay))
    for rand in asyncio.as_completed(desc):
        delay = await rand
        arr.append(delay)

    return arr
