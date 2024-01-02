#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False


def uppercase(s):
    for char in s:
        if islower(char):
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()
