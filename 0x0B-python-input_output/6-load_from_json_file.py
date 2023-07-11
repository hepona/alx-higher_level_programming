#!/usr/bin/python3
"""define function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, encoding="utf-8", mode="r") as file:
       return json.dumps(file.read())
