#!/usr/bin/python3
"""Enpty"""


def write_file(filename="", text=""):
    """returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
