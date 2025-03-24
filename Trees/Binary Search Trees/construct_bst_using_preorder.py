# Leetcode: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# https://www.youtube.com/watch?v=UmJT3j26t1I



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:

        def construct_bst(preorder, index_ref, upper_bound):
            if index_ref[0] >= len(preorder) or preorder[index_ref[0]] > upper_bound:
                return None

            node = TreeNode(preorder[index_ref[0]])
            index_ref[0] += 1
            node.left = construct_bst(preorder, index_ref, node.val)
            node.right = construct_bst(preorder, index_ref, upper_bound)
            return node
        
        return construct_bst(preorder, [0], float("+inf"))

        