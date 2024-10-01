#!/usr/bin/python3
import sys
from os.path import exists

# Import the save and load functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists
if exists(filename):
    # Load the existing list from the file
    items = load_from_json_file(filename)
else:
    # If the file does not exist, start with an empty list
    items = []

# Add all command line arguments (except the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
