#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the keys of the dictionary and sort them
    sorted_keys = sorted(a_dictionary.keys())
    
    # Print the dictionary items in the order of the sorted keys
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")

# Example usage
sample_dict = {
    "banana": 3,
    "apple": 5,
    "cherry": 2,
}
