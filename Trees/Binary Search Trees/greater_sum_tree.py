from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_binary_search_tree(arr):
    Q = deque()
    root = Node(int(arr[0]))
    Q.append(root)
    insert_nodes(Q, arr, 1)
    return root


def insert_nodes(Q, arr, index):
    len_ = len(arr)
    while True:
        if not Q:
            break
        top = Q.popleft()
        if index < len_:
            if arr[index] != "null":
                top.left = Node(int(arr[index]))
                Q.append(top.left)
            else:
                top.left = None
            index += 1
        if index < len_:
            if arr[index] != "null":
                top.right = Node(int(arr[index]))
                Q.append(top.right)
            else:
                top.right = None
            index += 1


def inorder_traversal(root, inorder_elements):
    if root is None:
        return
    inorder_traversal(root.left, inorder_elements)
    inorder_elements.append(root.data)
    inorder_traversal(root.right, inorder_elements)


def replace_node_data_with_greater_sum(root, num_sum_dict):
    if root is None:
        return
    replace_node_data_with_greater_sum(root.left, num_sum_dict)
    root.data = num_sum_dict[root.data]
    replace_node_data_with_greater_sum(root.right, num_sum_dict)


def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


if __name__ == "__main__":
    arr = input().split()
    root = build_binary_search_tree(arr)
    inorder_elements = []
    inorder_traversal(root, inorder_elements)
    sufix_sum = 0
    num_sum_dict = {}
    for num in inorder_elements[::-1]:
        sufix_sum += num
        num_sum_dict[num] = sufix_sum
    replace_node_data_with_greater_sum(root, num_sum_dict)
    preorder_traversal(root)
