from typing import List


def target_subarray_sum_longest(nums: List[int], target: int) -> int:
    left = 0
    subarry = []
    for right in range(len(nums)):
        subarry = nums[left:right+1]
        if sum(subarry) > target:
            left += 1

    return len(subarry)


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = target_subarray_sum_longest(nums, target)
    print(res)
