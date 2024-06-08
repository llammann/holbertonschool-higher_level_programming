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
    json_string = json.dumps(my_obj)

    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(json_string)
