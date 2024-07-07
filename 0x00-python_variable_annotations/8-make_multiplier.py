#!/usr/bin/env python3
"""Function make_multiplier that takes a float multiplier as an argument
and returns a function that multiplies a float by multiplier."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function make_multiplier that takes a float multiplier as an argument."""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply

if __name__ == "__main__":
    times_three = make_multiplier(3.0)
    print(times_three(10)) 
