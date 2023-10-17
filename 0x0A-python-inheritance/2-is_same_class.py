#!/usr/bin/python3
"""function that return True if the object is exactly an instance
False otherwise"""


def is_same_class(obj, a_class):
    """return true if the obj is an instance"""
    return type(obj) == a_class
