# Leetcode: https://leetcode.com/problems/binary-search-tree-iterator/description/
# Youtube: https://www.youtube.com/watch?v=D2jMcmxU4bs&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=51


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_all(root)

    def next(self) -> int:
        top_node = self.stack.pop()
        self.push_all(top_node.right)
        return top_node.val

    def hasNext(self) -> bool:
        return self.stack

    def push_all(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
