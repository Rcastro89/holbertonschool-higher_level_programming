#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if roman_string and isinstance(roman_string, str):
        values = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        for i in roman_string[::-1]:
            valor = values[i]
            if valor >= prev:
                total += valor
            else:
                total -= valor
            prev = valor
    return total
