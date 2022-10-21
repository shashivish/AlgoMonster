from typing import List


def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if feasible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def feasible(newspapers_read_times: List[int], num_coworkers: int, limit: int):
    time, no_workers = 0, 0
    for read_time in newspapers_read_times:
        if time + read_time > limit:
            time = 0
            no_workers += 1
        time += read_time

    if time != 0:
        no_workers += 1

    return no_workers <= num_coworkers




if __name__ == '__main__':
    newspapers_read_times = [7, 8, 5, 10, 2]
    num_coworkers = 2
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)
