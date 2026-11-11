def minimum_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


print(minimum_coins([1, 2, 5], 11))
print(minimum_coins([1, 3, 4], 6))
print(minimum_coins([2, 4], 7))
print(minimum_coins([1, 5, 10], 18))
