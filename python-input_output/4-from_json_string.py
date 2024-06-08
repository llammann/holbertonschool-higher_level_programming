#!/usr/bin/python3
"""
This module contains a function `from_json_string`.
"""

import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python data structure
        represented by the JSON string.
    """
    return json.loads(my_str)
