#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Determine fewest number of coins needed to meet a given amount

    Args:
        coins: list of the values of the coins
        total: total amount
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for coin in coins:
        while check < total:
            check += coin
            temp += 1
        if check == total:
            return temp
        check -= coin
        temp -= 1
    return -1
