#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list_f = set(my_list)
    for i in my_list_f:
        sum = sum + i
    return sum
