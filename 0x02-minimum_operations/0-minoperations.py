#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """
    Calculate the minimum operations needed to obtain a string of 'H' characters with a length of n.

    :param n: Target length of the string
    :return: Minimum operations needed
    """
    
    # Initialize variables
    next = 'H'       # Content currently stored in the clipboard
    body = 'H'       # Growing string of 'H' characters
    op = 0           # Count of operations performed
    
    # Continue operations until the length of the string 'H' reaches or exceeds the target length n
    while len(body) < n:
        # If the target length is divisible by the current length of the string 'H'
        if n % len(body) == 0:
            op += 2         # Copy and paste multiple times to optimally use the clipboard
            next = body     # Update the clipboard content
            body += body    # Extend the string by pasting the clipboard content
        else:
            op += 1         # Copy the current content of the clipboard
            body += next    # Paste the content of the clipboard

    # Check if the obtained string has the desired length
    if len(body) != n:
        return 0

    # Return the total number of operations needed to reach or exceed the target length
    return op


