#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    my_list_c = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list_c[i] = replace
    return my_list_c
