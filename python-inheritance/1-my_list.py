#!/usr/bin/python3
"pritn list"


class MyList(list):
    def print_sorted(self):
        "Sort the list in ascending order and print it"
        print(sorted(self))
