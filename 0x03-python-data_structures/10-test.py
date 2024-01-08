#!/usr/bin/python3

def test(list):	
    link_start = 0
    if list is None:
        return 1
    length = len(list)
    link_end = length -1
    if length == 1:
        return 1
    while (link_start < link_end):
        if list[link_start] != list[link_end]:
            return 0
        link_start += 1
        link_end -= 1

    return 1

print("Plaindrom" if test([1,2,3,1]) else "Not Plaindrom")
print("Plaindrom" if test(None) else "Not Plaindrom")
print("Plaindrom" if test([1]) else "Not Plaindrom")
print("Plaindrom" if test([1,2,1]) else "Not Plaindrom")
print("Plaindrom" if test([2,2]) else "Not Plaindrom")
print("Plaindrom" if test([1, 17, 972, 50, 98, 88, 50, 972, 17, 1]) else "Not Plaindrom")

