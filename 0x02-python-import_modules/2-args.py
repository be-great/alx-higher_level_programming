#!/usr/bin/python3
import sys
length = len(sys.argv)
if length == 1:
    print("{} arguments.".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
for x in range(1, length):
    print("{}: {}".format(x, sys.argv[x]))
