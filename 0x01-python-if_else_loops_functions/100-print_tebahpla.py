#!/usr/bin/python3
check = 1
for c in range(122, 96, -1):
    if check:
        print('{:c}'.format(c), end='')
        check = 0
    else:
        print('{:c}'.format(c - 32), end='')
        check = 1
