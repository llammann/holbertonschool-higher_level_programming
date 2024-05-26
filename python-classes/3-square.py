#!/usr/bin/python3
# 3-square.py
"""
This module defines a Square class with a private instance attribute 'size'.
The size must be an integer and greater than or equal to 0.
Includes a method to calculate the area of the square.
"""

class Square:
    """
    Represents a square with a specific size.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a specific size.

        Args:
            size (int): The size of a side of the square, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
