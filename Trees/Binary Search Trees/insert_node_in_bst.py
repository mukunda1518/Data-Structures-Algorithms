# Leetcode: https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Recursive
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root

        # Iterative

        if root is None:
            return TreeNode(val)
        curr = root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
        return root

