#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False


def uppercase(str):
    for i in range(len(str)):
        if islower(str[i]):
            str[i] = chr(ord(str[i]) - 32)
        print("{}".format(str[i]), end="")
