 #!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    
    Args:
        matrix: List of lists of int/float.
        div: The divisor (int/float).

    Returns:
        New matrix with elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats, 
                   if rows are not the same size, 
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Check if matrix is valid
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if elements are ints/floats
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows are the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform division and round to 2 decimals
    return [[round(elem / div, 2) for elem in row] for row in matrix]
