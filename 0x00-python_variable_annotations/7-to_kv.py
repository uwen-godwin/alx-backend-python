#!/usr/bin/env python3
"""
A module for creating tuples from a string and int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of the int/float.
    """
    return (k, float(v**2))
