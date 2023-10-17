#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if ln == 0:
        return None
    max = my_list[0]
    for i in range(ln):
        if i == ln - 1:
            break
        if max <= my_list[i + 1]:
            max = my_list[i + 1]
    return max
