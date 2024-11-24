#!/usr/bin/env python3
"""This is the header of the file""""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Parameters:
        matrix (list[list[int]]): the 2D matrix to be rotated.

    Returns:
        None
    """
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
