#!/usr/bin/python3

import sys

# Function to solve the N-queens puzzle
def solve(row, column):
    # Initialize the solver with an empty solution
    solver = [[]]
    
    # Iterate through each row to place queens recursively
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver

# Function to place a queen in the current row and update the solutions
def place_queen(q, column, prev_solver):
    # Generate new solutions by placing queens in the next column
    solver_queen = []
    for array in prev_solver:
        for x in range(column):
            # Check if placing a queen at (q, x) is safe
            if is_safe(q, x, array):
                solver_queen.append(array + [x])
    return solver_queen

# Function to check if placing a queen at (q, x) is safe in terms of column and diagonals
def is_safe(q, x, array):
    # Check if x is in the same column
    if x in array:
        return False
    else:
        # Check diagonals
        return all(abs(array[column] - x) != q - column for column in range(q))

# Function to initialize N and check command line arguments
def init():
    # Check command line arguments and initialize N
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        the_queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if the_queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return the_queen

# Main function to solve and print N-queens solutions
def n_queens():
    the_queen = init()
    solver = solve(the_queen, the_queen)
    
    # Print the solutions in a clean format
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)

if __name__ == '__main__':
    n_queens()
