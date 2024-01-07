#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence:
        b = len(sentence), sentence[0]
        return b
    else:
        b = len(sentence), None
        return b
