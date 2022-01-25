#!/usr/bin/python3
from lib2to3.pgen2 import token
from posixpath import split


def text_indentation(text):
    """tokens strings"""
    tokens = []
    fill = []
    if type(text) is not str:
        raise TypeError("text must be a string")
    for txt in text:
        if txt != ':' and txt != '?' and txt != '.':
        	fill.append(txt) 
        else:
            fill.append(txt)
            tokens.append(fill)
            fill = []
    tokens.append(fill)
    y = 0
    while y < len(tokens):
        x = 0
        while x < len(tokens[y]):
            if tokens[y][0] == ' ':
                tokens[y].pop(0)
                x += 1
            else:
                break
        y += 1
    y = 0
    while y < len(tokens) - 1:
        print(''.join(tokens[y]))
        print()
        y += 1
    print(''.join(tokens[y]), end='')
