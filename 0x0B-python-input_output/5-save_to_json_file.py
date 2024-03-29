#!/usr/bin/python3
"""function that writes an Object to a text file, using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation"""
    with open(filename, encoding="utf-8", mode="w") as file:
        return json.dump(my_obj, file)
