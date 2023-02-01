import heapq
from typing import List


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    heap = []
    for current_list in lists:
        heapq.heappush(heap, (current_list[0], current_list, 0))

    res = []
    while heap:
        val, current_list, position = heapq.heappop(heap)
        res.append(val)
        position += 1
        if position < len(current_list):
            heapq.heappush(heap, (current_list[position], current_list, position))

    return res


if __name__ == '__main__':
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(' '.join(map(str, res)))
