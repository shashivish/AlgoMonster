from typing import List


def generate_sums(weights, sums, sum, n, memo):
    if memo[n][sum]:
        return
    if n == 0:
        sums.add(sum)
        return
    generate_sums(weights, sums, sum, n - 1, memo)
    generate_sums(weights, sums, sum + weights[n - 1], n - 1, memo)

    memo[n][sum] = True


def knapsack_weight_only(weights: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    sums = set()
    n = len(weights)
    total_sum = sum(weights)
    memo = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    print(memo)
    generate_sums(weights, sums, 0, n, memo)
    return list(sums)


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    res = knapsack_weight_only(weights)
    res.sort()
    for i in range(len(res)):
        print(res[i], end='')
        if i != len(res) - 1:
            print(' ', end='')
    print()
