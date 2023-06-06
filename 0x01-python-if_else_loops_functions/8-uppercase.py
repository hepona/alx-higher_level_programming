#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122 and str is not None:
            char = chr(ord(str[i]) - 32)
            print("{}".format(char), end="\n" if i == (len(str) - 1) else "")
        else:
            print("{}".format(str[i]), end="\n" if i == (len(str) - 1) else " \n" if str is None else "")
