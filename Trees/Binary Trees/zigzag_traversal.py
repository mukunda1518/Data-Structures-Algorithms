# Leetcode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = []
        left_to_right = True
        Q = deque()
        Q.append(root)
        while len(Q) > 0:
            len_ = len(Q)
            elements = []
            for i in range(len_):
                node = Q.popleft()
                elements.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            if left_to_right:
                result.append(elements)
            else:
                result.append(elements[::-1])
            left_to_right = not left_to_right
        return result




from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        ltr = True
        while queue:
            size = len(queue)
            temp = [0] * size
            for i in range(size):
                node = queue.popleft()
                index = i if ltr else (size - i - 1)
                temp[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ltr = not ltr
            res.append(temp)
        return res

        