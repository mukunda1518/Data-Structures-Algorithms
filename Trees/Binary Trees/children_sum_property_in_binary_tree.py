# Youtube: https://www.youtube.com/watch?v=fnmisPM6cVo&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=30

# Time complexity : O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def change_binary_tree(root):
    if root is None:
        return
    children_sum = 0
    if root.left:
        children_sum += root.left
    if root.right:
        children_sum += root.right

    if children_sum >= root.data:
        root.data = children_sum

    if children_sum < root.data:
        if root.left:
            root.left.data = children_sum
        if root.right:
            root.right.data = children_sum

    change_binary_tree(root.left)
    change_binary_tree(root.right)

    total = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data
    if root.left or root.right:
        root.data = total
