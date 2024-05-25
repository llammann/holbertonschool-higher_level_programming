#!/usr/bin/python3

matry=[]
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, num in enumerate(row):
            if idx != len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
