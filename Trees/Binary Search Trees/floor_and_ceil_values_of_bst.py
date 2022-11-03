

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_ceil_value(root, val):
    ceil = None
    while root:
        if root.val == val:
            return root.val
        if root.val > val:
            ceil = root.val
            root = root.left
        else:
            root = root.right
    return ceil


def find_floor_value(root, val):
    floor = None
    while root:
        if root.val == val:
            return root.val
        if root.val < val:
            floor = root.val
            root = root.right
        else:
            root = root.left
    return floor


