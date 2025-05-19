#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.

    Args:
        matrix (list of lists of int or float): The matrix to divide.
        div (int or float): The number to divide by. Must not be 0.

    Returns:
        A new matrix with each element divided by div.
        Each result is rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If any element is not a number.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div in (float('inf'), float('-inf')):
        return [[0.0 for element in row] for row in matrix]

    return [[round(element / div, 2) for element in row] for row in matrix]
