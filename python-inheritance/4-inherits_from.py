#!/usr/bin/python3
"""
Module to check if object is an instance of a
class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
