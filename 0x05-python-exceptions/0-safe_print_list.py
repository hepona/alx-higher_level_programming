#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nw_list=[0] * x
    try:
        for i in range(0, x):
            nw_list[i] = my_list[i]
        return nw_list[i]
    except IndexError:
        return my_list
