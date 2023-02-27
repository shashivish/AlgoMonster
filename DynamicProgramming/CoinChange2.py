from typing import List
from math import inf


def combination(coins, sum, amount, start, memo):
    if sum == amount:
        return 1

    if sum > amount:
        return 0

    if memo[start][sum] != -1:
        return memo[start][sum]

    res = 0
    for i in range(start, len(coins)):
        res += combination(coins, sum + coins[i], amount, i, memo)

    memo[start][sum] = res

    return res


def coin_game(coins: List[int], amount: int) -> int:
    n = len(coins)
    memo = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]
    return combination(coins, 0, amount, 0, memo)


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_game(coins, amount)
    print(res)
