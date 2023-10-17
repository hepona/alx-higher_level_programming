#!/usr/bin/python3
"""function that return num of characters"""


def write_file(filename="", text=""):
    """return num of character"""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        myfile.write(text)
    with open(filename, mode="r", encoding="utf-8") as myfile:
        char_num = 0
        num_ch = len(myfile.read())
    return num_ch
