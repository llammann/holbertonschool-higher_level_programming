#!/usr/bin/python3
"""
Module: 2-matrix_divided

Function to divide elements of a matrix by a given number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists of int/float): The matrix.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix elements are not int/float or rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

