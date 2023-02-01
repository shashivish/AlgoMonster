from typing import List


def target_subarray_sum_fixed(nums: List[int], k: int) -> int:
    if k > len(nums):
        return 0
    if k == len(nums):
        return sum(nums)
    current_sum = 0

    end = k
    for i in range(len(nums)):
        if end < len(nums):
            subarry = nums[i: i + end]
            if sum(subarry) > current_sum:
                current_sum = sum(subarry)

    return current_sum


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = target_subarray_sum_fixed(nums, k)
    print(res)
