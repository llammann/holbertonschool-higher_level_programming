#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()

    for row in matrix:
        for idx, num in enumerate(row):
            if idx != len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
