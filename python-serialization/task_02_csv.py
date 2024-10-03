#!/usr/bin/python3
"""
This module converts a CSV file to JSON format.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts the data from a CSV file to JSON format
    and writes it to 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to be converted.
    """
    data = []

    try:
        """Open and read the CSV file."""
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            csvReader = csv.DictReader(csvfile)
            """Convert each row into a dictionary
            and append it to the data list."""
            for rows in csvReader:
                data.append(rows)

        """Write the data to a JSON file."""
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
            return True

    except Exception:
        return False
