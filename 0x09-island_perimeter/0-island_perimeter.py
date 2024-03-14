#!/usr/bin/python3
"""
Module defining the isWinner function.

This module contains functions related to determining the winner in a prime game.
"""

def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds in the game.
        nums (list of int): List of integers representing the number of prime
                             numbers to be removed in each round.

    Returns:
        str or None: The winner of the game ("Ben" or "Maria"), or None if the
                     input is invalid.
    """
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize scores for Ben and Maria
    ben = 0
    maria = 0

    # Create a list 'a' of length sorted(nums)[-1] + 1 with all elements
    # initialized to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]

    # The first two elements of the list, a[0] and a[1], are set to 0
    # because 0 and 1 are not prime numbers
    a[0], a[1] = 0, 0

    # Use Sieve of Eratosthenes algorithm to generate array of prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Play each round of the game
    for i in nums:
        # If the sum of prime numbers in the set is even, Ben wins
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list of int): The list of integers representing prime numbers.
        x (int): The prime number whose multiples need to be removed from ls.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
