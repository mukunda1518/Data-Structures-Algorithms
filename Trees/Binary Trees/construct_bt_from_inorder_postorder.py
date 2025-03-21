# Leetcode: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# https://www.youtube.com/watch?v=LgLRTaEMRVc



from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        n = len(inorder)
        in_map = { inorder[i]: i for i in range(n)}
        
        def consturct_tree(postorder, post_start, post_end, inorder, in_start, in_end, in_map):
            if post_start > post_end or in_start > in_end:
                return None
            
            node = TreeNode(postorder[post_end])
            in_root = in_map[postorder[post_end]]
            nums_left = in_root - in_start

            node.left = consturct_tree(postorder, post_start, post_start + nums_left - 1, inorder, in_start, in_root - 1, in_map)
            node.right = consturct_tree(postorder, post_start + nums_left, post_end - 1, inorder, in_root + 1, in_end, in_map)
            return node
        return consturct_tree(postorder, 0, n - 1, inorder, 0, n - 1, in_map)

        