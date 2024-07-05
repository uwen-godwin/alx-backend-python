#!/usr/bin/env python3
"""
A module for safely getting values from dictionaries.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value for the key in the dictionary if it exists, else default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
