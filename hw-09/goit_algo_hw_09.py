def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev = [-1] * (amount + 1)

    for coin in coins:
        for j in range(coin, amount + 1):
            if dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1
                prev[j] = coin

    result = {}
    while amount > 0:
        result[prev[amount]] = result.get(prev[amount], 0) + 1
        amount -= prev[amount]

    return result
