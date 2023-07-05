#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: .?:
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print("{}".format(i), end="")
        if i in [".", "?", ":"]:
            print("\n\n")
    print()
