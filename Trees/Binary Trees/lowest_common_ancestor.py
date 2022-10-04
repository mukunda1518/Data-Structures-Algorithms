# Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

from collections import deque
import sys

int_max = sys.maxsize

queue = deque()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(arr, root):
    for i in range(len(arr)):
        if arr[i] != "null":
            root = insert_node(arr[i], root)
        else:
            root = insert_node(int_max, root)
    root = remove_null_nodes(root)
    return root


def insert_node(data, root):
    new_node = Node(data)
    if len(queue) != 0:
        temp = queue[0]

    if root is None:
        root = new_node
    elif temp.left == None:
        temp.left = new_node
    elif temp.right == None:
        temp.right = new_node
        queue.popleft()

    if data != int_max:
        queue.append(new_node)
    return root

def remove_null_nodes(root):
    if root is None or root.data == int_max:
        return None
    root.left = remove_null_nodes(root.left)
    root.right = remove_null_nodes(root.right)
    return root

def find_lowest_common_ancestor(root, m, n):
    if root is None or root.data == m or root.data == n:
        return root
    left_root = find_lowest_common_ancestor(root.left, m , n)
    right_root = find_lowest_common_ancestor(root.right, m , n)
    
    if left_root and right_root:
        return root
    elif left_root:
        return left_root
    elif right_root:
        return right_root
    else:
        return None

if __name__ == "__main__":
    m, n = input().split()
    queue = deque()
    arr = [x for x in input().split()]
    root = None
    root = build_tree(arr, root)
    ancestor = find_lowest_common_ancestor(root, m, n)
    print(ancestor.data)
        
