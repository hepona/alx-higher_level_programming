#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not my_list :
        return 0
    s = 0
    for i in my_list:
        for j in my_list:
            s = s + (i * j)
            q = j + j
    r = s / q
    return r
