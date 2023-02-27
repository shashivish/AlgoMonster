import math
from typing import List
from math import inf


def min_coin(coins, amount, sum , memo):
    if sum == amount:
        return 0

    if sum > amount:
        return math.inf
    if memo[sum] != -1:
        return memo[sum]

    ans = math.inf
    for coin in coins:
        #print("Checking Coin : " , coin , " Sum : " , sum )
        result = min_coin(coins, amount, sum + coin , memo)
        if result == math.inf:
            continue
        #print(result)
        #print("Check Min of Ans and Result +1" , ans , result+1)
        ans = min(ans, result + 1)

    memo[sum]  = ans

    return ans


def coin_change(coins: List[int], amount: int) -> int:
    memo  = [-1] * (amount +1)
    result = min_coin(coins, amount, 0 , memo)
    if result == inf or None:
        return -1
    else:
        result


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
