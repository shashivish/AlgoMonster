from typing import List
from collections import deque


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def get_neighbors(node: int):
        return graph[node]

    def helper(root, target):
        queue = deque([root])
        level = 0
        visited = deque([root])
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return level
                for node in get_neighbors(node):
                    if node in visited:
                        continue
                    queue.append(node)
                    visited.append(node)
            level += 1
        return level

    return helper(a, b)


if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)
