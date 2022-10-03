# Leetcode: https://leetcode.com/problems/binary-tree-right-side-view/description/

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

def get_right_side_view_iterative_approach(root):
    res = []
    q = deque([root])
    while q:
        right_node = None
        len_ = len(q)
        for _ in range(len_):
            node = q.popleft()
            if node:
                right_node = node
                q.append(node.left)
                q.append(node.right)
        if right_node:
            res.append(right_node.data)
    print(*res)


def get_right_side_view_recurrsive_approach(root, level, right_side_view):
    if not root:
        return None
    if level == len(right_side_view):
        right_side_view.append(root.data)
        
    get_right_side_view_recurrsive_approach(root.right, level + 1, right_side_view)
    get_right_side_view_recurrsive_approach(root.left, level + 1, right_side_view)


if __name__ == "__main__":
    arr = [x for x in input().split()]
    root = None
    root = build_tree(arr, root)
    # get_right_side_view_iterative_approach(root)
    level = 0
    right_side_view = []
    get_right_side_view_recurrsive_approach(root, level, right_side_view)
    print(*right_side_view)
    
        
