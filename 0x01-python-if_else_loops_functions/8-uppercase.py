#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            let = ord(i) - 32
        else:
            let = ord(i)
        print("{}".format(chr(let)), end="")
    print("")
