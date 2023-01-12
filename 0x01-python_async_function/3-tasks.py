#!/usr/bin/env python3
"""Tasks 3."""


from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Ths function returns a asyncio.Task."""
    ctask = create_task(wait_random(max_delay))
    return ctask
