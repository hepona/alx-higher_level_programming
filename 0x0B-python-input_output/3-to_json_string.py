#!/usr/bin/python3
import json

"""function that return JSON representation of an object (string)"""


def to_json_string(my_obj):
    """return JSON representation of an object"""
    return json.dumps(my_obj)
