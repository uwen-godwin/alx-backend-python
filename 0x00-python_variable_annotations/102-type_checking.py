#!/usr/bin/env python3

"""
A module for type checking.
"""

from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Returns a list with elements repeated by the factor.
    
    Parameters:
    - lst: A tuple of any type of elements.
    - factor: An integer factor to repeat elements (default is 2).
    
    Returns:
    - A list of elements with each element repeated by the factor.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

if __name__ == "__main__":
    print(zoom_2x)
    print(zoom_3x)
