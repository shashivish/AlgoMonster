class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_valid_bst(root, lessThan, largerThan):
    if not root:
        return True
    if root.val <= largerThan or root.val >= lessThan:
        print("Current Root :", root.val)
        print("Current Less :", lessThan)
        print("Current Large : ", largerThan)
        print("Rule Broked.....")
        return False

    print("Current Root :", root.val)
    print("Current Less :", lessThan)
    print("Current Large : ", largerThan)

    print(f"Selected Less for Left Tree {lessThan} , {root.val}   is  = {min(lessThan,root.val)}")
    left_bst_result = check_valid_bst(root.left, min(lessThan, root.val), largerThan)

    print(f"Selected Max for Rigt Tree {largerThan} , {root.val}   is  = {max(largerThan,root.val)}")
    right_bst_result = check_valid_bst(root.right, lessThan, max(root.val, largerThan))
    return left_bst_result and right_bst_result


def valid_bst(root):
    return check_valid_bst(root, float('inf'), float('-inf'))


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    input = "6 4 3 x x 8 x x 8 x x"
    root = build_tree(iter(input.split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')
