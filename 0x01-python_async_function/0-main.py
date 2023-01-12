#!/usr/bin/env python3


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


print(f"t1  {asyncio.run(wait_random())}")
print(f" t2 {asyncio.run(wait_random(5))}")
print(f" t3 {asyncio.run(wait_random(15))}")
