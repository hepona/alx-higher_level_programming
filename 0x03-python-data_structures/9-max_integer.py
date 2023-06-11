#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    max = my_list[0]
    for i in range(ln):
        if ln == 0:
            return None
        if i == ln - 1:
            break
        if max <= my_list[i + 1]:
            max = my_list[i + 1]
    return max
