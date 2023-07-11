#!/usr/bin/python3
"""function that append string at the end of a text file"""


def append_write(filename="", text=""):
    """append txt at the end of a file"""
    with open(filename, encoding="utf-8", mode="a") as file:
        file.write(text)
    with open(filename, encoding="utf-8", mode="r") as file:
        num_char = len(file.read())
    return num_char
