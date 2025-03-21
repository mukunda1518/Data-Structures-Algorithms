# Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# https://www.youtube.com/watch?v=aZNaLrVebKQ



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(inorder)
        in_map = { inorder[i]: i for i in range(n)}
        
        def consturct_tree(preorder, pre_start, pre_end, inorder, in_start, in_end, in_map):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            node = TreeNode(preorder[pre_start])
            in_root = in_map[preorder[pre_start]]
            nums_left = in_root - in_start

            node.left = consturct_tree(preorder, pre_start + 1, pre_start + nums_left, inorder, in_start, in_root - 1, in_map)
            node.right = consturct_tree(preorder, pre_start + nums_left + 1, pre_end, inorder, in_root + 1, in_end, in_map)
            return node
        return consturct_tree(preorder, 0, n - 1, inorder, 0, n - 1, in_map)
