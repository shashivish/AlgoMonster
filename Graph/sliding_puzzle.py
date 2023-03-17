import collections
from typing import List


def num_steps(init_pos: List[List[int]]) -> int:
    start = tuple(tuple(line) for line in init_pos)
    move_count = {start: 0}
    target = ((1, 2, 3), (4, 5, 0))
    queue = collections.deque([start])

    def get_next_possible_positions(move, row, col):
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        all_moves = []
        for delta_row, delta_col in direction:
            new_row, new_col = row + delta_row, col + delta_col
            if new_row >= 0 and new_row < 2 and new_col >= 0 and new_col < 3:
                move_list = list(list(line) for line in move)
                move_list[new_row][new_col], move_list[row][col] = move_list[row][col], move_list[new_row][new_col]
                new_move = tuple(tuple(line) for line in move_list)
                all_moves.append(new_move)

        return all_moves

    visited = set()
    visited.add(start)
    while queue:
        move = queue.popleft()
        # print("Checking Move " , move)
        for i, line in enumerate(move):
            for j, value in enumerate(line):
                if value == 0:
                    row, col = i, j

        all_moves = get_next_possible_positions(move, row, col)
        for next_move in all_moves:
            if next_move not in visited:
                move_count[next_move] = move_count[move] + 1
                visited.add(next_move)
                queue.append(next_move)

                if next_move == target:
                    return move_count[target]

    return -1


if __name__ == '__main__':
    init_pos = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = num_steps(init_pos)
    print(res)
