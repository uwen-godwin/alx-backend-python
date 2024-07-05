#!/usr/bin/env python3

"""
A module for type checking.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list with elements repeated by the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
