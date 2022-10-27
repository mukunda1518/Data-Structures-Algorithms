# Leetcode: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/


from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):

        self.vertical_map = defaultdict(list)

        def dfs(root, col, row):
            if root is None:
                return
            self.vertical_map[col].append((root.val, row))
            if root.left:
                dfs(root.left, col - 1, row + 1)
            if root.right:
                dfs(root.right, col + 1, row + 1)

        dfs(root, 0, 0)
        result = []
        for col in sorted(self.vertical_map.keys()):
            self.vertical_map[col].sort(key=lambda x: (x[1], x[0]))
            result.append([tup[0] for tup in self.vertical_map[col]])
        return result
