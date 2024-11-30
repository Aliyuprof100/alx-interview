#!/usr/bin/python3


def makeChange(coins, total):
    # If total is 0 or less, return 0 as no coins are needed
    if total <= 0:
        return 0
    # Initialize dp array with a large number, to represent infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0
    # Iterate over each coin
    for coin in coins:
        # Update dp array for amounts from coin to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
