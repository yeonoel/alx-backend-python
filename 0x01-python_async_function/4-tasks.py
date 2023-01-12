#!/usr/bin/env python3
"""Module 4"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    return the list of all the delays(float values).
    """
    arr, desc = [], []

    for i in range(n):
        task_delay = task_wait_random(max_delay)
        task_delay.add_done_callback(lambda x: arr.append(x.result()))
        desc.append(task_delay)

    for rand in desc:
        await rand

    return
