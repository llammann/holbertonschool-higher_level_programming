#!/usr/bin/python3
"""
This module defines a class `Student`.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance with
        the given first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the student instance.

        Returns:
            dict: A dictionary containing
            the student's first name, last name, and age.
        """
        return self.__dict__
