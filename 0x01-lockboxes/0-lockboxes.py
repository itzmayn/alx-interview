#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    # Get the total number of boxes
    n = len(boxes)

    # Create a set to keep track of visited boxes
    visited = set()

    # Define a depth-first search (DFS) function
    def dfs(box_number):
        # If the box is already visited, return
        if box_number in visited:
            return
        
        # Mark the box as visited
        visited.add(box_number)
        
        # Explore all the boxes that can be opened from the current box
        for key in boxes[box_number]:
            dfs(key)

    # Start DFS from the first box (box number 0)
    dfs(0)

    # Check if all boxes have been visited
    return len(visited) == n

