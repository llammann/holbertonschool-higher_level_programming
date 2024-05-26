#!/usr/bin/python3
# 4-square.py
"""
This module defines a Square class with a private instance attribute 'size',
getter, and setter methods for size, and a method to calculate the area of
the square.
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
        self.size = size

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: The size of a side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): The size of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
