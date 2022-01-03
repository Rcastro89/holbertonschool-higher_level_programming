#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        list_tru_fal = my_list.copy()
        i = 0
        while i < len(my_list):
            if my_list[i] % 2 == 0:
                list_tru_fal[i] = 'True'
            else:
                list_tru_fal[i] = ''
            i += 1
    return list_tru_fal
