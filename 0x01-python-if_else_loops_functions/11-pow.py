#!/usr/bin/python3
def pow(a, b):
    r = 1
    if b == 0:
        return 1
    elif b < 0:
        b = b * -1
        for i in range(b):
            r = r * a
        return 1 / r
    else:
        for i in range(b):
            r = r * a
        return r
