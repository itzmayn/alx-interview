#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates the given n x n 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list): The 2D matrix to be rotated.
    """
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            # Save top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - i + first][first]

            # Move bottom element to left
            matrix[last - i + first][first] = matrix[last][last - i + first]

            # Move right element to bottom
            matrix[last][last - i + first] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top


