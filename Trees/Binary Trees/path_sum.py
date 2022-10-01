#   Leetcode : https://leetcode.com/problems/path-sum/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:

        def sum_path(root, target_sum, path_sum):
            if root is None:
                return 0
            path_sum += root.val

            if root.left is None and root.right is None:
                return target_sum == path_sum

            return sum_path(root.left, target_sum, path_sum) or sum_path(root.right, target_sum, path_sum)

        return sum_path(root, targetSum, 0)


