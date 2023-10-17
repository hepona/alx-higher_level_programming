#!/usr/bin/python3
def no_c(my_string):
    nw_string = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            nw_string = nw_string + my_string[i]
    return nw_string
