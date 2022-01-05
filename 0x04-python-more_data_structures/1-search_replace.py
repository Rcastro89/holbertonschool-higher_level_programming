#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        new_list = my_list.copy()
        j = 0
        for i in my_list:
            if i == search:
                new_list[j] = replace
            j += 1
    else:
        new_list = my_list
    return new_list
