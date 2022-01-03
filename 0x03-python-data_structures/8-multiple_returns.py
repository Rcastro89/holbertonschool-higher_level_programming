#!/usr/bin/python3
def multiple_returns(sentence):
    large = len(sentence)
    if large == 0:
        Letter = 'None'
    else:
        Letter = sentence[0]
    my_tuple = (large, Letter)
    return my_tuple
