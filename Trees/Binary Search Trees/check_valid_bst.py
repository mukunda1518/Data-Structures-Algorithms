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


def check_valid_bst_or_not(root, mini=float("-inf"), maxi=float("+inf")):
    if root is None:
        return True
    if root.data < mini or root.data > maxi:
        return False
    return check_valid_bst_or_not(root.left, mini, root.data - 1) and check_valid_bst_or_not(root.right, root.data + 1,
                                                                                             maxi)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()[0:-1]
        root = build_binary_search_tree(arr)
        is_valid_bst = check_valid_bst_or_not(root)
        if is_valid_bst:
            print(1)
        else:
            print(0)
