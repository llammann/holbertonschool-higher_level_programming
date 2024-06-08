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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student instance.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns:
            dict: A dictionary containing
            the requested attributes of the student.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):

            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }

        return self.__dict__
