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


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":
    arr = [x for x in input().split()]
    root = None
    root = build_tree(arr, root)
    preorder(root)


# [1 2 3 4 5 6]
# Output
# 12 20 13 15 14  - Preorder traversal


# [12 20 "null" 13 14 "null" 15 ]
# Output
# 12 20 13 15 14   - Preorder traversal

