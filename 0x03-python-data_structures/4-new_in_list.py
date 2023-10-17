#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cp = my_list.copy()
    if my_list is None:
        return None
    elif idx < 0 or idx >= len(my_list):
        return my_list_cp
    else:
        my_list_cp[idx] = element
        return my_list_cp
