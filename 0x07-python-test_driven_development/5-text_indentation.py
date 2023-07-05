#!/usr/bin/python3
"""
This is a simple module that print text with 2 new lines 
"""


def text_indentation(text):
    """function that print text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(" .", ".").replace(" ?", "?").replace(" :", ":")
    text = text.replace(". ", ".").replace("? ", "?").replace(": ", ":")
    for i in text:
        print("{}".format(i), end="")
        if i in [".", "?", ":"]:
            print("\n", end="")
    print()
