#!/usr/bin/python3
"""function that read a file"""


def read_file(filename=""):
    """read a file"""
    with open(filename, mode="r",  encoding="utf-8") as myfile:
        print(myfile.read(), end="")
