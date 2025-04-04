# Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:  # No Need of this base condition
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

        # Iterative
        node = root
        while node:
            val = node.val
            if val > p.val and val > q.val:
                node = node.left
            elif val < p.val and val < q.val:
                node = node.right
            else:
                return node
        return node
