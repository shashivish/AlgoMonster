class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_bst(bst: Node, val: int) -> Node:
    if bst is None:
        bst = Node(int(val), None, None)
        return bst

    if val > bst.val:
        # call right tree
        new_node  = insert_bst(bst.right, val)
        bst.right = new_node
    elif val < bst.val:
        # call left tree
        new_node = insert_bst(bst.left, val)
        bst.left = new_node
    else:
        # Case where val matched with Node . No need to insert again
        return bst

    return bst


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)


if __name__ == '__main__':
    input = "8 4 2 1 x x 3 x x 6 x x 12 10 x x 14 x 15 x x"
    val = 7
    bst = build_tree(iter(input.split()), int)
    # val = int(input())
    res = insert_bst(bst, val)
    print(' '.join(format_tree(res)))
