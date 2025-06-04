#!/usr/bin/python3
"""
Module: task_02_csv

Read data from a CSV file, converts it to JSON format,
and saves it to data.json
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format, saving to 'data.json'.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        True if succesful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r") as f:
            reader = csv.DictReader(f)
            data_list = [row for row in reader]

        with open("data.json", mode="w") as f:
            json.dump(data_list, f)
        return True
    except Exception:
        return False
