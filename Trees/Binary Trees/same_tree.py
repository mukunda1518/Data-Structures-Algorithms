# Leetcode: https://leetcode.com/problems/same-tree/
# https://www.youtube.com/watch?v=BhuvF_-PWS0&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=18


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
