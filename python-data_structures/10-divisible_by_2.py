#!/usr/bin/python3


result = []


def divisible_by_2(my_list=[]):
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
