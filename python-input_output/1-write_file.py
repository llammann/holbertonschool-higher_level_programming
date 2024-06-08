#!/usr/bin/python3
"""
This module contains a function `write_file`
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
        filename (str): The file name
        text (str): The text

    Returns:
        int: The number of characters.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
