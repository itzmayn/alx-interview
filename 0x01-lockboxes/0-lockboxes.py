#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """
   # Check if input is a list
    if type(boxes) is not list:
        return False

    # Check if the list is empty
    elif len(boxes) == 0:
        return False

    # Iterate through the keys starting from 1 (assuming 0 is already unlocked)
    for key in range(1, len(boxes) - 1):
        # Initialize a flag to check if the key can open any box
        boxes_checked = False

        # Iterate through the boxes
        for idx in range(len(boxes)):
            # Check if the key can open the box and the key is not the same as the box index
            boxes_checked = key in boxes[idx] and key != idx

            # If the key can open the box, exit the inner loop
            if boxes_checked:
                break

        # If the key cannot open any box, return False
        if not boxes_checked:
            return boxes_checked

    # If all keys can open corresponding boxes, return True
    return True


