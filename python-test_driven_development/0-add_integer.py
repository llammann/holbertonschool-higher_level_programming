#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int, float): The first number. Must be an integer or a float.
        b (int, float): The second number. Must be an integer or a float.
        Default is 98.

    Returns:
        int: The sum of a and b, cast to an integer if they are floats.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
