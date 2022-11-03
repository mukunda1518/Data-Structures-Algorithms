# Leetcode: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Youtube: https://www.youtube.com/watch?v=sWf7k1x9XR4&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=39


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flatten_using_stack(root):
            if not root:
                return root
            stack = [root]
            while stack:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                if stack:
                    node.right = stack[-1]
                node.left = None
            return root

        prev = None

        def flatten_using_recursion(root):
            if root is None:
                return

            flatten_using_recursion(root.right)
            flatten_using_recursion(root.left)

            nonlocal prev
            root.right = prev
            root.left = None
            prev = root

        def flatten_with_constant_space(root):
            curr = root
            while curr:
                if curr.left:
                    prev = curr.left
                    while prev.right:
                        prev = prev.right
                    prev.right = curr.right
                    curr.right = curr.left
                    curr.left = None
                curr = curr.right

        return flatten_using_stack(root)

        flatten_using_recursion(root)
        return root

        flatten_with_constant_space(root)
        return root








