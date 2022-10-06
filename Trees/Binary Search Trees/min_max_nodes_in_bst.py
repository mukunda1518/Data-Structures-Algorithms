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
    root = None
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


def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


if __name__ == "__main__":
    arr = input().split()  # Given Nodes in level order traversal
    root = None
    root = build_tree(arr, root)   #  5 4 8 -4 null null 9 null -3 7
    min_num = get_minimum_value(root)
    max_num = get_maximum_value(root)
    print(min_num, max_num)
    preorder_traversal(root)



