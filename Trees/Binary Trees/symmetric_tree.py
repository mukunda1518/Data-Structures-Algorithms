# Leetcode: https://leetcode.com/problems/symmetric-tree/

# https://www.youtube.com/watch?v=nKggNAiEpBE&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=25


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False
    
        def is_symmetric_help(l_node, r_node):
            if l_node is None or r_node is None:
                return l_node == r_node
            
            if l_node.val != r_node.val:
                return False
            
            return is_symmetric_help(l_node.left, r_node.right) and is_symmetric_help(l_node.right, r_node.left)
        
        return is_symmetric_help(root.left, root.right)
        