# Leetcode: https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def get_min_val_node(self, ptr):
        while ptr.left:
            ptr = ptr.left
        return ptr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # return self.delete_node_recursive(root, key)
        return self.delete_node_iterative(root, key)

    # Iterative Solution
    def delete_node_iterative(self, root, key):
        temp = root
        if root is None:
            return None
        if root.val == key:
            return self.helper(root)
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return temp

    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        right_child = root.right
        last_right_child = self.get_last_right_child(root.left)
        last_right_child.right = right_child
        return root.left

    def get_last_right_child(self, root):
        if root.right is None:
            return root
        return self.get_last_right_child(root.right)

    # Recursive Solution
    def delete_node_recursive(self, root, key):
        if root is None:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left and root.right:
                successor = self.get_min_val_node(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
            else:
                child = root.right if root.right else root.left
                root = child
        return root



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def helper(self, root):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            return root.left


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root and root.val == key:
            return self.helper(root)
        node = root
        while node:
            if key < node.val:
                if node.left and node.left.val == key:
                    node.left = self.helper(node.left)
                    break
                else:
                    node = node.left
            else:
                if node.right and node.right.val == key:
                    node.right = self.helper(node.right)
                    break
                else:
                    node = node.right
        return root


        
        

