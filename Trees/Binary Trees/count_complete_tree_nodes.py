# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        def get_total_no_of_nodes(root):
            if root is None:
                return 0

            lh = get_left_height(root)
            rh = get_right_height(root)

            if lh == rh:
                return pow(2, lh) - 1

            return 1 + get_total_no_of_nodes(root.left) + get_total_no_of_nodes(root.right)

        return get_total_no_of_nodes(root)
