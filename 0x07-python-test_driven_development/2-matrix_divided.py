#!/usr/bin/python3

"""
Module : function that divides all elements of a matrix.
matrix must be a matrix (list of lists) of integers/floats
"""


def matrix_divided(matrix, div):
    """
    args: list(int/floats) matrix ,(int)div
    """

    if matrix is None or len(matrix) == 0:
        error = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(error)
    check = all(
        isinstance(row, list) and all(isinstance(column, (int, float))
                                      for column in row)
        for row in matrix
        )
    if not check:
        error = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(error)

    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is not equal to 0 and is int and float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(column / div, 2) for column in rows]
        for rows in matrix
        ]
    return new_matrix
