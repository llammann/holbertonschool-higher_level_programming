#!/usr/bin/python3
"""
This module defines a Square class with private instance attributes
'size' and 'position'.
Includes methods to calculate the area of the square
and print it with a given position.
"""


class Square:
    """
    Represents a square with a specific size and position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a specific size and position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character # at a given position.
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
