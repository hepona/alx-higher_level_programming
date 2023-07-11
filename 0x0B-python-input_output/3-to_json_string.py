#!/usr/bin/python3
"""function that return JSON representation of an object (string)"""


import json

def to_json_string(my_obj):
    """return JSON representation of an object"""
    return json.dumps(my_obj)
