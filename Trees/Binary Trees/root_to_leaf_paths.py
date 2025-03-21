


from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def get_all_paths(self, root, temp, res):
        if root is None:
            return

        temp.append(root.data)

        if root.left is None and root.right is None:
            res.append(temp[:])
    
        else:
            self.get_all_paths(root.left, temp, res)
            self.get_all_paths(root.right, temp, res)

        temp.pop()
        
        
    def Paths(self, root):
        res = []
        self.get_all_paths(root, [], res)
        return res
    
   
def get_path_to_node(self, root, target, temp):
    if not root:
        return False # Stop if node is None

    temp.append(root.data)

    if root.data == target:  # If target is found, return True
        return True

    if self.get_path_to_node(root.left, target, temp) or \
        self.get_path_to_node(root.right, target, temp):
            return True     # Stop further recursion

    temp.pop()  # Remove only if the target was NOT found
    return False    # Indicate that target was not found in this path
    
    
