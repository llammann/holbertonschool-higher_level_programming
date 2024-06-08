#!/usr/bin/python3
"""
This module contains a function `save_to_json_file`.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename: The file name.
    """
    try:
        json_string = json.dumps(my_obj)
    except TypeError as e:
        print(f"[TypeError] {e}")
        return

    try:
        with open(filename, 'w') as file:
            file.write(json_string)
    except PermissionError as e:
        print(f"[PermissionError] {e}")
        print(f"[PermissionError] {filename}")
