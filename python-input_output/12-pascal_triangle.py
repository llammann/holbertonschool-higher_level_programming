#!/usr/bin/python3
"""
This module defines a function `pascal_triangle`.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print Pascal's triangle.

    Args:
        triangle (list): List of lists representing Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
