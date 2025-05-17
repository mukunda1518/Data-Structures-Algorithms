# Find the size of the largest BST in binary tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_largest_bst_size_in_binary_tree(root):
    # max_node, min_node, max_size = float("-inf"), float("+inf"), 0

    def find_largest_bst(root):
        # An empty tree is BST of size 0
        if root is None:
            return (float("-inf"), float("+inf"), 0)

        # Get values of left and right subtree of current tree
        left_tup = find_largest_bst(root.left)
        right_tup = find_largest_bst(root.right)

        # current node is greater than max in left AND smaller than min in right
        if left_tup[0] < root.val and root.val < right_tup[1]: # it is BST
            return (max(root.val, right_tup[0]), min(root.val, left_tup[1]), left_tup[2] + right_tup[2] + 1)
                    # max_value, min_value, size
        else:
            # It is not BST, max as INT_MAX and min as INT_MIN, size = max(left, right)
            return (float("+inf"), float("-inf"), max(left_tup[2], right_tup[2]))

    tup_ = find_largest_bst_size_in_binary_tree(root)
    return tup_[2]  # returns size


# By using classes

class Nodeval:

    def __init__(self, min_node, max_node, max_size):
        self.min_node = min_node
        self.max_node = max_node
        self.max_size = max_size


def find_largest_bst(root):
    # An empty tree is BST of size 0
    if root is None:
        # (min, max, size)
        return Nodeval(float("+inf"), float("-inf"), 0)

    # Get values of left and right subtree of current tree
    left = find_largest_bst(root.left)
    right = find_largest_bst(root.right)

    # current node is greater than max in left AND smaller than min in right
    if left.max_node < root.val and root.val < right.min_node:  # it is BST
        return Nodeval(min(root.val, left.min_node), max(root.val, right.max_node), left.max_size + right.max_size + 1)
            # max_value, min_value, size
    else:
        # It is not BST, max as INT_MAX and min as INT_MIN, size = max(left, right)
        return Nodeval(float("-inf"), float("+inf"), max(left.max_size, right.max_size))
