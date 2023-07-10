#!/usr/bin/python3
"""function that return True if the object is exactly an instance
False otherwise"""

def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
