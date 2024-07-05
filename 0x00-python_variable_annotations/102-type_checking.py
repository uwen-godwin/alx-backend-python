#!/usr/bin/env python3

"""
A module for type checking.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a list with elements repeated by the factor.
    
    Parameters:
    - lst: A tuple of integers.
    - factor: An integer factor to repeat elements (default is 2).
    
    Returns:
    - A list of integers with each element repeated by the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
