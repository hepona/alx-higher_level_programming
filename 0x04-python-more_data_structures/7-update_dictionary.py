#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) == 0:
        return a_dictionary
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary.update({key: value})
    return a_dictionary
