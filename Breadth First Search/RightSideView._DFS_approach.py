from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root: Node) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    def helper(root, depth, data_list):
        if root is None:
            return None
        if len(data_list) == depth:
            data_list.append(root.val)

        right = helper(root.right, depth + 1, data_list)
        left = helper(root.left, depth + 1, data_list)

        return data_list
    data_list = helper(root, 0, [])

    return data_list


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
