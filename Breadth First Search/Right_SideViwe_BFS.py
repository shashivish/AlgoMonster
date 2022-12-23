from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root):
    res = []
    queue = deque([root])  # at least one element in the queue to kick start bfs
    while len(queue) > 0:  # as long as there is element in the queue
        n = len(queue)  # number of nodes in current level
        print(queue[0].val)
        res.append(queue[0].val)  # only append the first node we encounter since it's the rightmost
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            for child in [node.right, node.left]:  # add right child first so it'll pop out of the queue first
                if child is not None:
                    queue.append(child)
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
    root = build_tree(iter("1 2 4 x 7 x x 5 x x 3 x 6 x x".split()), int)
    res = binary_tree_right_side_view(root)
    print(' '.join(map(str, res)))
