#!/usr/bin/python3
"""
This module defines a class `Student`.
"""


class Student:
    """
    Represents a student with attributes first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with first name, last name, and age.

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
                          If None, retrieve all attributes.

        Returns:
            dict: A dictionary containing
            the requested attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):

            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        else:
            return {}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from a dictionary.

        Args:
            json (dict): A dictionary where keys are
            attribute names and values are attribute values.
        """
        for key in json:
            self.__dict__.update({key: json[key]})


def main():
    pass


if __name__ == "__main__":
    main()
