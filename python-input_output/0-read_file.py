#!/usr/bin/python3
"""Enpty"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
