#!/usr/bin/python3
"""define function that creates an Object from a “JSON file"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, encoder="utc-8", mode="w") as file:
        json.load(file)
