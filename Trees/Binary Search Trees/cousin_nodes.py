from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_bst(arr):
    Q = deque()
    root = Node(int(arr[0]))
    Q.append(root)
    insert_nodes(Q, arr, 1)
    return root


def insert_nodes(Q, arr, index):
    while True:
        if not Q:
            break
        top = Q.popleft()
        if index < len(arr):
            if arr[index] != "null":
                top.left = Node(int(arr[index]))
                Q.append(top.left)
            else:
                top.left = None
            index += 1
        if index < len(arr):
            if arr[index] != "null":
                top.right = Node(int(arr[index]))
                Q.append(top.right)
            else:
                top.right = None
            index += 1


def get_level_and_parent_of_node(root, val, level=0, prev=None):
    if root.data == val:
        return (level, prev)
    prev = root
    if val < root.data:
        return get_level_and_parent_of_node(root.left, val, level + 1, prev)
    else:
        return get_level_and_parent_of_node(root.right, val, level + 1, prev)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n = map(int, input().split())
        arr = input().split()
        root = build_bst(arr)
        m_level, m_parent = get_level_and_parent_of_node(root, m)
        n_level, n_parent = get_level_and_parent_of_node(root, n)
        if m_level == n_level and m_parent != n_parent:
            print(1)
        else:
            print(0)


