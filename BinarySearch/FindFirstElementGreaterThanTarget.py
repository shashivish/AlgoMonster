from typing import List


def first_not_smaller(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    position = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
            position = mid
        else:
            left = mid + 1

    return position


if __name__ == '__main__':
    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2
    res = first_not_smaller(arr, target)
    print(res)
