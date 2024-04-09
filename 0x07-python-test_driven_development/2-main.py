#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix0 = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix1 = [
    [1, 2],
    [4, 5],
    [7, 8]
]
matrix2 = [
    [1, 2],
    [4],
    [7, 8]
]

print(matrix_divided(matrix0, 3))
print(matrix0)


print(matrix_divided(matrix1, 3))
print(matrix1)

print(matrix_divided(matrix2, 3))
print(matrix2)
