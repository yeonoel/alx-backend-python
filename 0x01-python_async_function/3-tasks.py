#!/usr/bin/env python3
"""Tasks 3."""


from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Ths function returns a asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
