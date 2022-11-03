# Leetocde: https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Recurrsive

        if root is None:
            return None
        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)

        # Iterative

        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root

