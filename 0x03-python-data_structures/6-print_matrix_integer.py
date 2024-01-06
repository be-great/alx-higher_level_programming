#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if len(matrix[0]) != 0:
        for x in matrix:
            col = len(x)
            for i in range(col):
                if i == col - 1:
                    print("{:d}".format(x[i]), end="\n")
                else:
                    print("{:d}".format(x[i]), end=" ")
    else:
        print()
