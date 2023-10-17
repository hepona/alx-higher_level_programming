#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("{}".format(str))
    for i in range(0, len(str)):
        res = ''
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            char = chr(ord(str[i]) - 32)
            res = res + char
        else:
            res = str[i]

        print("{}".format(res), end="\n" if i == (len(str) - 1) else "")
