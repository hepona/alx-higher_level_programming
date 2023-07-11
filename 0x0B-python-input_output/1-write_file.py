#!/usr/bin/python3
"""function that return num of characters"""


def write_file(filename="", text=""):
    """return num of character"""
    with open(filename, mode="r+",  encoding="utf-8") as myfile:
        myfile.write(text)
        char_num = 0
        while 1:
            charead = myfile.read(1)
            if charead != '\n':
                char_num = char_num + 1
                if not charead:
                    break
    return char_num