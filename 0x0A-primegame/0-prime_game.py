#!/usr/bin/python3
"""
Module defining isWinner function.
"""

def isWinner(x, nums):
    """
    Function to determine the winner in the prime game.

    Parameters:
    x (int): Some parameter description.
    nums (list): Some parameter description.

    Returns:
    str or None: The winner of the game, either "Winner: Maria" or "Winner: Ben",
    or None if there is no winner.
    """
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while True:
            if not primesSet:
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"
    elif mariaWinsCount < benWinsCount:
        return "Winner: Ben"
    else:
        return None


def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.

    Parameters:
    n (int): The number to be checked for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """
    Returns a list of prime numbers in the range [start, end].

    Parameters:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).

    Returns:
    list: A list of prime numbers in the specified range.
    """
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes
