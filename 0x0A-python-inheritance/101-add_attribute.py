#!/usr/bin/python3
def add_attribute(obj, name, value):
    """function that add attibute if possible"""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
