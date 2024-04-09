#!/usr/bin/python3
"""
Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

"""
import sys


def initialize_chessboard(size):
    """Initialize an `size`x`size` sized chessboard with 0's."""
    chessboard = [[' ' for _ in range(size)] for _ in range(size)]
    return chessboard


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    result = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == "Q":
                result.append([x, y])
                break
    return (result)


def deep_copy_chessboard(board):
    """copy the chessboard"""
    if isinstance(board, list):
        return list(map(deep_copy_chessboard, board))
    return board


def x_position_ouput(board, row, col):
    """
    x spot on the board
    """
    # x in forward position
    for x in range(col + 1, len(board)):
        board[row][x] = "x"
    # x in backwards position
    for x in range(col - 1, -1, -1):
        board[row][x] = "x"
    # x in position down
    for x in range(row + 1, len(board)):
        board[x][col] = "x"
    # x in position above
    for x in range(row - 1, -1, -1):
        board[x][col] = "x"
    # x in spots diagonally down on the right
    n = col + 1
    for x in range(row + 1, len(board)):
        if n >= len(board):
            break
        board[x][n] = "x"
        n += 1
    # x in spots diagonally up on the left
    n = col - 1
    for x in range(row - 1, -1, -1):
        if n < 0:
            break
        board[x][n]
        n -= 1
    # x in spots diagonally up on the right
    n = col + 1
    for x in range(row - 1, -1, -1):
        if n >= len(board):
            break
        board[x][n] = "x"
        n += 1
    # x in spots diagonally down to the left
    n = col - 1
    for x in range(row + 1, len(board)):
        if n < 0:
            break
        board[x][n] = "x"
        n -= 1


def recursive_solve(board, row, queens, results):
    """
    Recursively solve an N-queens puzzle.
    """
    if queens == len(board):
        results.append(get_solution(board))
        return (results)

    for y in range(len(board)):
        if board[row][y] == " ":
            new_board = deep_copy_chessboard(board)
            new_board[row][y] = "Q"
            x_position_ouput(new_board, row, y)
            results = recursive_solve(new_board, row + 1, queens + 1, results)

    return (results)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
