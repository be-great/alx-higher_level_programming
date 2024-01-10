#!/usr/bin/python3

def roman_to_int(roman_string):
    # check if roman_string is string or it's none
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_v = 0

    for num in reversed(roman_string):
        value = roman_dict[num]
        if value < prev_v:
            total -= value
        else:
            total += value
        prev_v = value

    return total
