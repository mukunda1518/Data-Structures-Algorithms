# Youtube: https://www.youtube.com/watch?v=fnmisPM6cVo&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=30

# Time complexity : O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def change_binary_tree(root):
    if root is None:
        return
    children_sum = 0
    if root.left:
        children_sum += root.left
    if root.right:
        children_sum += root.right

    if children_sum >= root.data:
        root.data = children_sum

    if children_sum < root.data:
        if root.left:
            root.left.data = children_sum
        if root.right:
            root.right.data = children_sum

    change_binary_tree(root.left)
    change_binary_tree(root.right)

    total = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data
    if root.left or root.right:
        root.data = total



# Geeks for Geeks

# https://www.geeksforgeeks.org/problems/children-sum-parent/1


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        def dfs(node):
            if not node:
                return 1
            if not node.left and not node.right:
                return 1
            
            l_val = node.left.data if node.left else 0
            r_val = node.right.data if node.right else 0
            
            if l_val + r_val != node.data:
                return 0
        
            return dfs(node.left) and dfs(node.right)
    
        return dfs(root)
    

# Making all the nodes to follow Children Sum Property in Binary Tree 


class Solution:
    def main_child_sum(self, root):
        # # Making all the nodes to follow Children Sum Property in Binary Tree 
        def dfs(node):
            if not node:
                return 
            
            c_sum = 0
            if node.left:
                c_sum += node.left.val
            if node.right:
                c_sum += node.right.val
            
            if node.val < c_sum:
                node.val = c_sum
            else:
                if node.left:
                    node.left.val = c_sum
                if node.right:
                    node.right.val = c_sum
            
            dfs(node.left)
            dfs(node.right)
        
            total = 0
            
            if node.left:
                total += node.left.val
            if node.right:
                total += node.right.val
            
            if node.left or node.right:
                node.val = total

        dfs(root)
        return root

