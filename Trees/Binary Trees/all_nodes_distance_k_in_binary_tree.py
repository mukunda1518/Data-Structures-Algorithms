# Leetcode: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

#
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_track = {}

        def track_the_parent_of_nodes(root):
            dq = deque()
            dq.append(root)
            parent_track[root] = None

            while dq:
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    parent_track[node.left] = node
                if node.right:
                    dq.append(node.right)
                    parent_track[node.right] = node

        def get_nodes_at_distance_k(target, k):
            dist = 0
            dq = deque()
            visited = set()
            visited.add(target)
            dq.append(target)
            res = []

            while dq:
                if dist == k:
                    break
                dist += 1
                size = len(dq)
                for i in range(size):
                    node = dq.popleft()
                    if node.left and node.left not in visited:
                        dq.append(node.left)
                        visited.add(node.left)
                    if node.right and node.right not in visited:
                        dq.append(node.right)
                        visited.add(node.right)
                    if parent_track[node] and parent_track[node] not in visited:
                        dq.append(parent_track[node])
                        visited.add(parent_track[node])
            while dq:
                node = dq.popleft()
                res.append(node.val)
            return res

        track_the_parent_of_nodes(root)
        return get_nodes_at_distance_k(target, k)
