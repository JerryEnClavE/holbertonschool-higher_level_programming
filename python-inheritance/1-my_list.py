#!/usr/bin/python3
"""Inherits from list and adds a method to print the list in sorted order."""



class MyList(list):
    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        print(sorted(self))
