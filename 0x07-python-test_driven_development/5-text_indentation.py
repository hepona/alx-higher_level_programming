#!/usr/bin/python3
"""
This is a simple module that provides a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print("{}".format(i), end="")
        if i in [".", "?", ":"]:
            print("\n")
    print()
