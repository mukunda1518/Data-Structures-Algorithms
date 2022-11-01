# Leetcode: https://leetcode.com/problems/binary-tree-paths/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root):
        res = []

        def dfs(root, s):
            if root.left is None and root.right is None:
                s += str(root.val)
                res.append(s)
                return
            s += str(root.val) + "->"

            if root.left:
                dfs(root.left, s)

            if root.right:
                dfs(root.right, s)

        dfs(root, "")
        return res

        # To check path from root to any node
        res1 = []

        def check_path(root, res1, val=5):
            if root is None:
                return False

            res1.append(root.val)

            if root.val == val:
                return True

            if check_path(root.left, res1, val) or check_path(root.right, res1, val):
                return True

            res1.pop()
            return False

        check_path(root, res1, 6)
        return res1
