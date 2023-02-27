from typing import List


# LeetCode : https://leetcode.com/problems/triangle/description/

# DFS + Memoization Solution

def dfs(row, col, memo):
    if row == len(triangle):
        return 0

    if memo[row][col] != - 1:
        return memo[row][col]

    left = dfs(row + 1, col, memo)
    right = dfs(row + 1, col + 1, memo)

    sum = triangle[row][col] + min(left, right)

    memo[row][col] = sum

    return sum


def minimum_total(triangle: List[List[int]]) -> int:
    n = len(triangle)

    memo = [[-1] * len(triangle) for _ in range(len(triangle))]

    return dfs(0, 0, memo)


if __name__ == '__main__':
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)
