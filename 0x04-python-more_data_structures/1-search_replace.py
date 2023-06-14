#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    if search-1 > len(my_list) or search-1 < 0:
        return my_list
    my_list_c = my_list.copy()
    my_list_c[search - 1] = replace
    return my_list_c
