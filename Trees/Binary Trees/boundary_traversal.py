# Leetcode: https://leetcode.com/problems/boundary-of-binary-tree/description/

# https://www.youtube.com/watch?v=0ca1nvR0be4&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=20



from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def is_leaf(self, root: Optional[TreeNode]) -> bool:
        if root:
            return not root.left and not root.right
        return False
    
    def get_leaf_nodes(self, root: Optional[TreeNode], res: list[int]) -> list[int]:
        if root is None:
            return
        if self.is_leaf(root):
            res.append(root.val)
            return

        self.get_leaf_nodes(root.left, res)
        self.get_leaf_nodes(root.right, res)

    def get_left_nodes(self, root, res):
        curr = root.left
        while curr:
            if not self.is_leaf(curr):
                res.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    def get_right_nodes(self, root, res):
        curr = root.right
        temp = []
        while curr:
            if not self.is_leaf(curr):
                temp.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])

    
    def boundary_traversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        res = []
        if not self.is_leaf(root):
            res.append(root.val)

        self.get_left_nodes(root, res)
        self.get_leaf_nodes(root, res)
        self.get_right_nodes(root, res)

        return res
