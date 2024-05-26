#!/usr/bin/python3
# 1-square.py
"""
This module defines a Square class with a private instance attribute 'size'.
"""


class Square:
    """
    Represents a square with a specific size.
    """
    
    
    def __init__(self, size):
        """
        Initializes the square with a specific size.
        """
        self.__size = size
