# Leetcode : https://leetcode.com/problems/delete-node-in-a-bst/description/

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
    for val in arr:
        if val != "null":
            root = insert_node(int(val), root)
        else:
            root = insert_node(int_max, root)
    root = remove_null_nodes(root)
    return root


def insert_node(val, root):
    new_node = Node(val)
    if len(queue) != 0:
        temp = queue[0]
    if root is None:
        root = new_node
    elif temp.left is None:
        temp.left = new_node
    elif temp.right is None:
        temp.right = new_node
        queue.popleft()

    if val != int_max:
        queue.append(new_node)
    return root


def remove_null_nodes(root):
    if root is None or root.data == int_max:
        return None
    root.left = remove_null_nodes(root.left)
    root.right = remove_null_nodes(root.right)
    return root


def get_minimum_value(root):
    if root.left is None:
        return root.data
    return get_minimum_value(root.left)


def get_maximum_value(root):
    if root.right is None:
        return root.data
    return get_maximum_value(root.right)


def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


def get_max_val_node(ptr):
    while ptr.right:
        ptr = ptr.right
    return ptr


def delete_node(root, k):
    if root is None:
        return None
    elif k < root.data:
        root.left = delete_node(root.left, k)
    elif k > root.data:
        root.right = delete_node(root.right, k)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left and root.right:
            predecesor = get_max_val_node(root.left)
            root.data = predecesor.data
            root.left = delete_node(root.left, predecesor.data)
        else:
            child = root.left if root.left else root.right
            root = child
    return root


def get_min_val_node(ptr):
    while ptr.left:
        ptr = ptr.left
    return ptr


def delete_node_successor(root, key):
    if root is None:
        return None
    elif key < root.data:
        root.left = delete_node_successor(root.left, key)
    elif key > root.data:
        root.right = delete_node_successor(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left and root.right:
            successor = get_min_val_node(root.right)
            root.data = successor.data
            root.right = delete_node_successor(root.right, successor.data)
        else:
            child = root.right if root.right else root.left
            root = child
    return root


if __name__ == "__main__":
    k = int(input())
    arr = input().split()
    root = None
    root = build_tree(arr, root)
    # By replacing predecesor node
    root = delete_node(root, k)
    postorder_traversal(root)




