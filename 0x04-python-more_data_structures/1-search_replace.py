#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    if search > len(my_list) or search <= 0:
        return my_list
    my_list_c = my_list.copy()
    my_list_c[search - 1] = replace
    return my_list_c
