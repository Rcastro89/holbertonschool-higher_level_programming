#!/usr/bin/python3
"""pascal"""


def pascal_triangle(n):
    """return list of list pascal"""
    pascal = []
    for i in range(1, n + 1):
        pascal_fill = []
        for j in range(1, i + 1):
            if len(pascal) >= 2:
                try:
                    act = pascal[i - 2][j - 1]
                except Exception:
                    act = 0
                ant = (0 if (j - 2) < 0 else pascal[i - 2][j - 2])
                temp = act + ant
                pascal_fill.append(temp)
            else:
                pascal_fill.append(1)
        pascal.append(pascal_fill)
    return pascal
