#!/usr/bin/env python3
"""
A module for sum of mixed list.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.
    """
    return sum(mxd_lst)
