from typing import List
def find_first_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    position = -1

    while left <= right:
        mid = (left + right) // 2
        print("Found Mid Element : ", mid)

        if arr[mid] == target:
            right = mid - 1
            position = mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return position


if __name__ == '__main__':
    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
    res = find_first_occurrence(arr, target)
    print(res)
