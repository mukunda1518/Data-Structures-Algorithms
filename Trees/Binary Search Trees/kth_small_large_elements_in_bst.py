# Leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Youtube: https://www.youtube.com/watch?v=9TJYWh0adfk&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=46
# https://takeuforward.org/data-structure/kth-largest-smallest-element-in-binary-search-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def find_kth_smallest(root, arr):
            if root is None:
                return None
            left = find_kth_smallest(root.left, arr)
            if left is not None:
                return left
            arr[0] -= 1
            if arr[0] == 0:
                return root.val
            return find_kth_smallest(root.right, arr)

        return find_kth_smallest(root, [k])

        def find_kth_largest(root, arr):
            if root is None:
                return None
            right = find_kth_largest(root.right, arr)
            if right:
                return right
            arr[0] -= 1
            if arr[0] == 0:
                return root.val
            return find_kth_largest(root.left, arr)

        return find_kth_largest(root, [k])




