# Leetcode: https://leetcode.com/problems/diameter-of-binary-tree/description/

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

def longest_path_between_two_nodes(root):
    max_path = 0
    def longest_path(root):
        if not root:
            return -1
        left_count = longest_path(root.left) + 1 
        right_count = longest_path(root.right) + 1 
        nonlocal max_path
        max_path = max(max_path, left_count + right_count)
        return max(left_count, right_count)
    longest_path(root)
    return max_path

if __name__ == "__main__":
    arr = [x for x in input().split()]
    root = None
    root = build_tree(arr, root)
    print(longest_path_between_two_nodes(root))
        
