from typing import List

from collections import deque


def count_number_of_islands(grid: List[List[int]]) -> int:
    num_rows, num_col = len(grid), len(grid[0])

    def find_surrounding_node(node_coordinate):
        visited_list = []
        r, c = node_coordinate
        d_row = [-1, 0, 1, 0]
        d_col = [0, 1, 0, -1]
        for i in range(len(d_row)):
            neighbour_r = r + d_row[i]
            neighbour_c = c + d_col[i]
            if 0 <= neighbour_r < num_rows and 0 <= neighbour_c < num_col:
                visited_list.append((neighbour_r, neighbour_c))

        return visited_list

    def helper(node, visited_node):
        queue = deque([node])
        r, c = node
        visited_node[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            visited_list = find_surrounding_node(node)
            print("Node ", node)
            print("Neighbour ", visited_list)
            for v in visited_list:
                r, c = v
                if grid[r][c] == 0 or visited_node[r][c]:
                    continue
                queue.append(v)
                visited_node[r][c] = True

    visited_node = list(list())
    for i in range(num_rows):
        tmp = []
        for j in range(num_col):
            tmp.append(False)
        visited_node.append(tmp)
    counter = 0
    for r in range(num_rows):
        for c in range(num_col):
            if grid[r][c] == 0 or visited_node[r][c]:
                continue
            helper((r, c), visited_node)
            counter += 1

    return counter


if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)
