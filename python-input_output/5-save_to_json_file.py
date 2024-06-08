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
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
