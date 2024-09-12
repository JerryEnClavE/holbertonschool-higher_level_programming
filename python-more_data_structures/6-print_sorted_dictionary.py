#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
sample_dict = {
    "banana": 3,
    "apple": 5,
    "cherry": 2,
}
