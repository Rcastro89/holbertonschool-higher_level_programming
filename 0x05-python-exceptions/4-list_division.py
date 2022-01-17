#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            add = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            add = 0
        except TypeError:
            print("wrong type")
            add = 0
        except IndexError:
            print("out of range")
            add = 0
        finally:
            new_list.append(add)
    return (new_list)
