# Leetcode: https://leetcode.com/problems/find-bottom-left-tree-value/

from collections import deque
import sys

int_max = sys.maxsize


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


queue = deque()


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


def get_bottom_left_node_value_using_queue(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return node.data

def get_bottom_left_node_value_using_stack(root):
    if not root:
        return
    
    max_depth = 0 
    stack = [(root, 1)]
    while stack:
        curr, level = stack.pop()
        if level > max_depth:
            max_depth = level
            ans = curr.data
        if curr.right:
            stack.append((curr.right, level + 1))
        if curr.left:
            stack.append((curr.left, level + 1))
    return ans


if __name__ == "__main__":
    arr = [x for x in input().split()]
    root = None
    root = build_tree(arr, root)
    print(get_bottom_left_node_value_using_stack(root))
    print(get_bottom_left_node_value_using_queue(root))
