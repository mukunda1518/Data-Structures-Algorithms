# Leetcode : https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import deque
import sys

int_max = sys.maxsize

Q = deque()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_binary_tree(root, arr):
    root = None
    for i in range(len(arr)):
        if arr[i] != "null":
            root = insert_node(arr[i], root)
        else:
            root = insert_node(int_max, root)
    root = remove_null_nodes(root)
    return root

def insert_node(data, root):
    new_node = Node(data)
    if len(Q) != 0:
        temp = Q[0]

    if root is None:
        root = new_node
    elif temp.left == None:
        temp.left = new_node
    elif temp.right == None:
        temp.right = new_node
        Q.popleft()
    if data != int_max:
        Q.append(new_node)
    return root
    
def remove_null_nodes(root):
    if root is None or root.data == int_max:
        return None
    root.left = remove_null_nodes(root.left)
    root.right = remove_null_nodes(root.right)
    return root
def get_depth_apporoach1(root):
    if root is None:
        return 0
    left_depth = get_depth_apporoach1(root.left)
    right_depth = get_depth_apporoach1(root.right)
    return max(left_depth, right_depth) + 1


# Repetition of code comparision occurs here
def get_depth_apporach2(root, level=0):
    if root is None:
        return level
    left_length = get_depth_apporach2(root.left, level + 1)
    right_length = get_depth_apporach2(root.right, level + 1)
    return max(left_length, right_length)

# Iterative apporach

def get_depth_by_iterative_apporach(root):
    stack = [(root, 1)]
    while stack:
        node, length = stack.pop()
        if length > depth:
            depth = length
        if node.right:
            stack.append( (node.right, length+1) )
        if node.left:
            stack.append( (node.left, length+1) )
    return depth
    
if __name__ == "__main__":
    arr = input().split()
    root = None
    root = build_binary_tree(root, arr)
    depth = get_depth_apporoach1(root)
    print(depth)