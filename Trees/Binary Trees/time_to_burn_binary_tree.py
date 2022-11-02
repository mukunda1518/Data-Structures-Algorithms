# Leetcode: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

# Youtube: https://www.youtube.com/watch?v=2r5wLmQfD6g&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=32


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_track = {}

        def track_the_parent_of_nodes(root, start):
            dq = deque()
            dq.append(root)
            parent_track[root] = None
            target = None

            while dq:
                node = dq.popleft()
                if node.val == start:
                    target = node
                if node.left:
                    dq.append(node.left)
                    parent_track[node.left] = node
                if node.right:
                    dq.append(node.right)
                    parent_track[node.right] = node
            return target

        def get_nodes_at_distance_k(target):
            dist = 0
            dq = deque()
            visited = set()
            visited.add(target)
            dq.append(target)

            while dq:
                size = len(dq)
                flag = 0   # to know at least we have burnt one node
                for i in range(size):
                    node = dq.popleft()
                    if node.left and node.left not in visited:
                        flag = 1
                        dq.append(node.left)
                        visited.add(node.left)
                    if node.right and node.right not in visited:
                        flag = 1
                        dq.append(node.right)
                        visited.add(node.right)
                    if parent_track[node] and parent_track[node] not in visited:
                        flag = 1
                        dq.append(parent_track[node])
                        visited.add(parent_track[node])
                if flag:
                    dist += 1
            return dist

        start = track_the_parent_of_nodes(root, start)
        return get_nodes_at_distance_k(start)