from typing import List


def move_zeros(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(' '.join(map(str, nums)))
