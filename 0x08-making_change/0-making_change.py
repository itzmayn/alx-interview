#!/usr/bin/python3
""" Dynamic Programming - Minimum Coin Change """

def makeChange(coins, total):
    """ Find the fewest number of coins needed to reach a given total amount.

    Args:
        coins (list): List of coin denominations available.
        total (int): Target total amount.

    Returns:
        int: Minimum number of coins needed to achieve the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met by any combination of available coins.

    Notes:
        - The coin values are integers greater than 0.
        - You can assume an infinite number of each coin denomination.
        - The solution's runtime will be evaluated for performance.
    """
    if total <= 0:
        return 0

    check = 0
    temp = 0
    coins.sort(reverse=True)

    for i in coins:
        while check < total:
            check += i
            temp += 1

        if check == total:
            return temp

        check -= i
        temp -= 1

    return -1
