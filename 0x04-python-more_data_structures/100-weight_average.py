#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not my_list :
        return 0
    s = 0
    q = 0
    for i in my_list:
        s = s + (i[0] * i[1])
        q = q + i[1]
    r = s / q
    return r
