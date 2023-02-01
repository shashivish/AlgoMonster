from collections import deque


def get_knight_shortest_path(x: int, y: int) -> int:
    def find_surrounding_node(node_coordinate):
        visited_list = []
        r, c = node_coordinate
        delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
        for i in range(len(delta_row)):
            neighbour_r = r + delta_row[i]
            neighbour_c = c + delta_col[i]
            visited_list.append((neighbour_r, neighbour_c))

        return visited_list

    def helper(node):
        queue = deque([node])
        visited_node = set()
        step = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                r,c = node
                if r == x and c == y:
                    # Do something break
                    return step
                visited_list = find_surrounding_node(node)
                for v in visited_list:
                    if v in visited_node:
                        continue
                    queue.append(v)
                    visited_node.add(v)
            step += 1

    return helper((0, 0))



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    res = get_knight_shortest_path(x, y)
    print(res)
