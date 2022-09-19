#!/usr/bin/python3
"""
Module add_integer
Adds two integers.
"""

def add_integer(a, b=98):
    """Adds two integers."""
    if type(a) is not [int, float]:
        raise TypeError('a must be an integer')
    if type(b) is not [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
