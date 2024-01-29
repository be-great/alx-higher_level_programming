#!/usr/bin/python3
"""
module :  function that prints a text
with 2 new lines after each of these characters
 ., ? and :
"""


def text_indentation(text):
    """
    args : (str)test
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    # Skip leading spaces
    while index < len(text) and text[index] == ' ':
        index += 1
    # Loop through the text
    while index < len(text):
        # Print the current character
        print(text[index], end="")
        # Check for newline or specific characters ('.', '?', ':')
        if text[index] == "\n" or text[index] in ".?:":
            # Add two new lines after '.', '?', or ':'
            if text[index] in ".?:":
                print("\n")

            # Move to the next character after the special character
            index += 1

            # Skip any additional spaces
            while index < len(text) and text[index] == ' ':
                index += 1

            # Continue to the next iteration of the loop
            continue

        # Move to the next character
        index += 1
