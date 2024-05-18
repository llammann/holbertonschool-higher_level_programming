#!/usr/bin/python3

def pow(a, b):
    result = a * b
    if b % 2 == 0:
        result = abs(result)
    return result
