#!/usr/bin/python3
"""Change comes from within
"""


def makeChange(coins, total):
    """Find the minimum number of coins required to achieve
    a specified total amount,
    using a collection of coins with varying denominations.
    """
    if total <= 0:
        return 0
    remainder = total
    coin_index = 0
    coins_count = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remainder > 0:
        if coin_index >= n:
            return -1
        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1
    return coins_count
