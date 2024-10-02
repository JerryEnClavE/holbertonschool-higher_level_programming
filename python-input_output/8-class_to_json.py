#!/usr/bin/python3
"""Python executable file."""


def class_to_json(obj):
    """Function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object."""

    result = {}
    for key, value in obj.__dict__.items():
        result[key] = value
    return result
