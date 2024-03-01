#!/usr/bin/python3
""" Coin Change Algorithm """

def make_change(coins, total):
    """ Find the minimum number of coins needed to reach a specific total amount.

    Args:
        coins (list): List of available coin denominations.
        total (int): The target total amount.

    Returns:
        int: Minimum number of coins required to achieve the total, or -1 if not possible.
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
