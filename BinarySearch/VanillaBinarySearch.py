def binary_search(arr: list[int], target: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = int((start + end) / 2)
        print(f"start : {start} , end : {end} , mid : {mid}")
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == '__main__':
    # Time Complexity: O(log(n))
    sorted_list = [10 ,20]
    target = 20
    print(binary_search(sorted_list, target))
