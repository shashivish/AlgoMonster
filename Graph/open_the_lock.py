from typing import List
from collections import deque

next_digit = {**{str(i): str(i + 1) for i in range(9)}, "9": "0"}
prev_digit = {e: n for n, e in next_digit.items()}


# print("Next Digit Dictionary :", next_digit)
# print("Previous Digit : " , prev_digit)


def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    if target_combo == "0000":
        return 0
    trapped_combos_set = set(trapped_combos)
    steps = {
        "0000": 0
    }

    bfs_queue = deque({"0000"})
    while bfs_queue:
        top = bfs_queue.popleft()
        for i in range(4):
            new_combo = top[0:i] + next_digit[top[i]] + top[i + 1:]
            # print("New Combo : ", new_combo)
            if new_combo not in trapped_combos_set and new_combo not in steps:
                bfs_queue.append(new_combo)
                steps[new_combo] = steps[top] + 1
                if new_combo == target_combo:
                    return steps[new_combo]
            new_combo = top[0:i] + prev_digit[top[i]] + top[i + 1:]
            # print("Another New Combo : ", new_combo)
            if new_combo not in trapped_combos_set and new_combo not in steps:
                bfs_queue.append(new_combo)
                steps[new_combo] = steps[top] + 1
                if new_combo == target_combo:
                    return steps[new_combo]
        # print("Queue List : ", bfs_queue)
    return -1


if __name__ == '__main__':
    target_combo = input()
    trapped_combos = input().split()
    res = num_steps(target_combo, trapped_combos)
    print(res)
