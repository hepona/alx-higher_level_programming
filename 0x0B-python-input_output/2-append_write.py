#!/usr/bin/python3
"""function that append string at the end of a text file"""
def append_write(filename="", text=""):
    """append txt at the end of a file"""
    with open(filename, encode = "utf-8", mode = "a") as file:

