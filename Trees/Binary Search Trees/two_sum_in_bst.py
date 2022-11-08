# Leetcode: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# Youtube: https://www.youtube.com/watch?v=ssL3sHwPeb4&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=52


# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.st_left = []
        self.st_right = []
        self.push_left(root)
        self.push_right(root)

    def push_left(self, node):
        while node:
            self.st_left.append(node)
            node = node.left

    def push_right(self, node):
        while node:
            self.st_right.append(node)
            node = node.right

    def left_next(self):
        top_node = self.st_left.pop()
        self.push_left(top_node.right)
        return top_node.val

    def right_next(self):
        top_node = self.st_right.pop()
        self.push_right(top_node.left)
        return top_node.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return
        bst = BSTIterator(root)
        left, right = bst.left_next(), bst.right_next()
        while left < right:
            if left + right < k:
                left = bst.left_next()
            elif left + right > k:
                right = bst.right_next()
            elif left + right == k:
                return True
        return False


