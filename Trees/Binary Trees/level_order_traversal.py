# Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/

# https://www.youtube.com/watch?v=EoAsWbO7sqg&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=8



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            l_data = []
            for i in range(n):
                node = queue.popleft()
                l_data.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(l_data)
        return res
