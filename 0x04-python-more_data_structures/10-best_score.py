#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = 0
        key = ""
        for i in a_dictionary:
            if a_dictionary[i]:
                if a_dictionary[i] > val:
                    val = a_dictionary[i]
                    key = i
        if key not in a_dictionary:
            return None
        else:
            return key
