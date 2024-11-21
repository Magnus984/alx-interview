#!/usr/bin/python3
"""
Rotate 2D Matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n * n 2D matrix 90 degrees clockwise
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: isinstance(x, list), matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    y, x = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if x == -1:
            x = rows - 1
            y += 1
        matrix[-1].append(matrix[x][y])
        if y == cols - 1 and x >= -1:
            matrix.pop(x)
        x -= 1
