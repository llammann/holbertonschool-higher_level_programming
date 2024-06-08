#!/usr/bin/python3
"""
This module contains a function `class_to_json`.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    """

    return obj.__dict___
