from typing import List
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root: Node) -> List[List[int]]:
    queue = deque([root])
    res = []
    flag = True
    while len(queue) > 0:
        tmp_list = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp_list.append(node.val)
            for node in [node.left, node.right]:
                if node is not None:
                    queue.append(node)
        if not flag:
            tmp_list.reverse()
        res.append(tmp_list)
        flag = not flag

    return res


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter("1 2 4 x 7 x x 5 x 8 x x 3 x 6 x x".split()), int)
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
