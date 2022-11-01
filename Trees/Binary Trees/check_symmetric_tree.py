# Leetcode: https://leetcode.com/problems/symmetric-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:

        def isMirror(l_tree, r_tree):
            if l_tree is None or r_tree is None:
                return l_tree == r_tree
            if l_tree.val != r_tree.val:
                return False
            return isMirror(l_tree.left, r_tree.right) and isMirror(l_tree.right, r_tree.left)

        return isMirror(root.left, root.right)
