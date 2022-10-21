from typing import List


def peak_of_mountain_array(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    position = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1] :
            position = mid
            right = mid - 1
        else:
            left = mid + 1
    return position


if __name__ == '__main__':
    arr = [0 ,10, 3, 2, 1, 0]
    res = peak_of_mountain_array(arr)
    print(res)
