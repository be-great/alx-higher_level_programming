#!/usr/bin/python3
import sys
length = len(sys.argv)
if length == 1:
    print("{} arguments.".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
for i, arg in enumerate(sys.argv[1:]):
    print("{}: {}".format(i + 1, arg))
