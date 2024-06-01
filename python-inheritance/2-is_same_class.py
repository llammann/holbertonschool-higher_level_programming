#!/usr/bin/python3
"""
module that cointains function to check if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """Method that return True if an object is an instance of a class"""

    return type(obj) is a_class
