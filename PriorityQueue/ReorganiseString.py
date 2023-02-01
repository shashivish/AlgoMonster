import heapq
from collections import Counter


def reorganize_string(s: str) -> str:
    n = len(s)
    str_count = Counter(s)
    heap = [[-val, key] for key, val in str_count.items()]
    heapq.heapify(heap)

    if -heap[0][0] > (n + 1 // 2):
        return ""

    res = [None] * n
    position = 0
    while heap:
        cnt, val = heapq.heappop(heap)
        cnt = -cnt
        for _ in range(cnt):
            res[position] = val
            position += 2

            if position >= n:
                position = 1
        print(res)
    return "".join(res)


if __name__ == '__main__':
    s = input()
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i + 1}")
            exit()
    print("Valid")
