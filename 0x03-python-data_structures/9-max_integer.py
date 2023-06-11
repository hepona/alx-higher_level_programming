#!/usr/bin/python3
def max_integer(my_list=[]):
    l = len(my_list)
    max = my_list[0]
    if len(my_list) == 0:
        return None
    for i in range(l):
        if i == l - 1:
            break
        if max <= my_list[i + 1]:
            max = my_list[i + 1]
    return max
