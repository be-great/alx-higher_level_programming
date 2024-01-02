#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        digit = number % 10
    else:
        digit = -1 * (number % -10)
    print("{}".format(digit), end='')
    return digit
