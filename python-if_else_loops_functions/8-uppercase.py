#!/usr/bin/python3
def uppercase(str):
    for char in str:
        temp = ord(char)
        if temp >= 97 and temp <= 122:
            temp = temp - 32
        print("{}".format(chr(temp)), end="")
    print("")
