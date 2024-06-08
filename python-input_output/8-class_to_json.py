#!/usr/bin/python3
"""
This module contains a function `class_to_json`.
"""

import json


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary representing the JSON serializable attributes
        of the object.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            json_dict[key] = value
    return json_dict
