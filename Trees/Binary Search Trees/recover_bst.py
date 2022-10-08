# Leetcode: https://leetcode.com/problems/recover-binary-search-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = middle = last = None

        def check_swap_nodes_by_inorder_traversal(root):
            if root is None:
                return
            check_swap_nodes_by_inorder_traversal(root.left)
            nonlocal prev
            print(root.val, prev.val)
            if prev and prev.val > root.val:
                nonlocal first, middle, last
                # print(prev.val, root.val)
                if first is None:
                    first = prev
                    middle = root
                else:
                    last = root
            prev = root
            # print(root.val, prev.val)
            check_swap_nodes_by_inorder_traversal(root.right)

        prev = TreeNode(float("-inf"))
        check_swap_nodes_by_inorder_traversal(root)

        if first and last:
            # print(first.val, last.val)
            first.val, last.val = last.val, first.val
        else:
            # print(first.val, middle.val)
            first.val, middle.val = middle.val, first.val

