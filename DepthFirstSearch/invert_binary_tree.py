class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    if tree == None :
        return None


    left_node = invert_binary_tree(tree.left)
    right_node = invert_binary_tree(tree.right)

     #Swap Node Values 
    temp_node = tree.left
    tree.left = right_node
    tree.right = temp_node

    return tree

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
    input = "1 2 4 x x 5 6 x x x 3 x x"
    tree = build_tree(iter(input.split()), int)
    res = invert_binary_tree(tree)
    print(' '.join(format_tree(res)))
