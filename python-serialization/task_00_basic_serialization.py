#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize the data (Python dictionary) to a JSON file and save it."""
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """Deserializes a JSON file into a Python dictionary."""
    with open(filename, "r") as json_file:
        return json.load(json_file)
