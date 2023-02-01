from typing import List


# LeetCode : https://leetcode.com/problems/partition-equal-subset-sum/description/


def target_exists(n, nums, target_sum, current_sum, dp):
    if current_sum == target_sum:
        return True
    if n == 0 or current_sum > target_sum:
        return False
    if dp[n][current_sum] != 0:
        if dp[n][current_sum] == 1:
            return True
        else:
            return False

    exists = target_exists(n - 1, nums, target_sum, current_sum + nums[n - 1], dp) or \
             target_exists(n - 1, nums, target_sum, current_sum, dp)

    if exists:
        dp[n][current_sum] = 1
    else:
        dp[n][current_sum] = 2

    return exists


def can_partition(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    n = len(nums)
    target = total_sum // 2
    # dp[i][j] = 0 : value not computed yet
    # dp[i][j] = 1 : value computed and is True
    # dp[i][j] = 2 : value computed and is False
    dp = [[0 for i in range(target + 1)] for _ in range(n + 1)]
    return target_exists(n, nums, target, 0, dp)


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = can_partition(nums)
    print('true' if res else 'false')
