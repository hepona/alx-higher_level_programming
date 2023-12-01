#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    if len(list_of_integers) == 0:
            return "None"
    res = []
    for i in range(len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] > list_of_integers[i + 1]:
                res.append(list_of_integers[i])
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i - 1]:
                res.append(list_of_integers[i])
        else:
            if (
                list_of_integers[i] > list_of_integers[i + 1]
                and list_of_integers[i] > list_of_integers[i - 1]
            ):
                res.append(list_of_integers[i])
    return str(res).strip('[]')
