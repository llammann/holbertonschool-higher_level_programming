#!/usr/bin/python3
"""
This module contains a function `read_file`
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str): The file name
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
