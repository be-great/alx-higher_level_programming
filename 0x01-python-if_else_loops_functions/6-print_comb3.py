#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):
        print(f"{x}{y}", end="")
        if (x + y != 17):
            print(", ", end="")
print("")
