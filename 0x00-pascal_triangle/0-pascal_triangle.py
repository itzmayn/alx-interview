#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    
    Args:
        n (int): The number of rows for Pascal's Triangle
    
    Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.
              Returns an empty list if n is less than or equal to 0.
    """
    # Initialize an empty list to store Pascal's Triangle
    triangle = []

    if n <= 0:
        return triangle  # Return an empty list if n is less than or equal to 0

    # The first row of Pascal's Triangle always contains 1
    triangle = [[1]]

    # Generate subsequent rows of Pascal's Triangle
    for i in range(1, n):
        row = [1]  # Initialize the row with the first element as 1

        # Calculate each element of the row based on the previous row
        for j in range(len(triangle[i - 1]) - 1):
            curr_row = triangle[i - 1]  # Reference to the previous row
            row.append(curr_row[j] + curr_row[j + 1])

        row.append(1)  # Append the last element as 1 to complete the row
        triangle.append(row)  # Add the row to the triangle

    return triangle  # Return the generated Pascal's Triangle
