# Leetcode: https://leetcode.com/problems/merge-two-binary-trees/submissions/812487832/

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


def add_two_binary_trees(root1, root2):
    if not root1 and not root2:
        return None
    if root1 and root2:
        val = int(root1.data) + int(root2.data)
        root1_left, root2_left = root1.left, root2.left
        root1_right, root2_right = root1.right, root2.right
    elif root1 and not root2:
        val = int(root1.data)
        root1_left, root2_left = root1.left, None
        root1_right, root2_right = root1.right, None
    elif root2 and not root1:
        val = int(root2.data)
        root1_left, root2_left = None, root2.left
        root1_right, root2_right = None, root2.right
    new_root = Node(val)
    new_root.left = add_two_binary_trees(root1_left, root2_left)
    new_root.right = add_two_binary_trees(root1_right, root2_right)
    return new_root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def add_two_binary_trees_approach2(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    root1.data = int(root1.data) + int(root2.data)

    root1.left = add_two_binary_trees_approach2(root1.left, root2.left)
    root1.right = add_two_binary_trees_approach2(root1.right, root2.right)
    return root1


if __name__ == "__main__":
    arr1 = [x for x in input().split()][0:-1]
    arr2 = [x for x in input().split()][0:-1]
    root1, root2 = None, None
    root1 = build_tree(arr1, root1)
    queue = deque()
    root2 = build_tree(arr2, root2)
    new_root = None
    # new_root = add_two_binary_trees(root1, root2)
    add_two_binary_trees_approach2(root1, root2)
    inorder(root1)