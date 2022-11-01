# Leetcode: https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append((root, 0))  # stores node and number at which nodes exists in its level
        width = 0
        while dq:
            start_node = dq[0]
            end_node = dq[-1]
            diff = end_node[1] - start_node[1] + 1
            width = max(width, diff)
            min_val = dq[0][1]
            for i in range(len(dq)):
                node, val = dq.popleft()
                val = val - min_val
                if node.left:
                    dq.append((node.left, 2 * val + 1))
                if node.right:
                    dq.append((node.right, 2 * val + 2))
        return width


