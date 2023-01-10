#!/usr/bin/env python3
"""Complex types - string and int/float to tuple."""


from typing import Tuple


def to_kv(k: str, v: int | float): Tuple[str, float]:
    """This function takes a string k and an
       int OR float v as arguments and returns a tuple.
    """
    return (k, v*v)
