from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    list_of_path = []

    def travelTree(root, path, list_of_path):

        if all(c is None  for c in root.children):
            list_of_path.append('->'.join(path) +'->' +str(root.val))
            return

        for child in root.children:
            if child is not None:
                travelTree(child, path + [str(root.val)], list_of_path)


    travelTree(root , [] ,list_of_path)
    #print("list_of_path" ,list_of_path)
    return list_of_path


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


if __name__ == '__main__':
    input = "1 3 2 1 5 0 3 0 4 0"
    root = build_tree(iter(input.split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
