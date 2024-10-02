#!/usr/bin/python3
"""Python executable file."""


class Student:
    """Student class creation."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that converts instance into JSON format."""
        result = {}
        if attrs is not None:
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value
        else:
            for key, value in self.__dict__.items():
                result[key] = value
        return result
