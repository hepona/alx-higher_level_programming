#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp = a_dictionary.copy()
    for i in (cp):
        cp[i] = cp[i] * 2
    return cp
