from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_nodes(arr, root, i, n):
    if i < n:
        node = Node(arr[i])
        root = node
        root.left = insert_nodes(arr, root.left, 2 * i + 1, n)

        root.right = insert_nodes(arr, root.right, 2 * i + 2, n)
    return root


def get_depth(node):
    d = 0
    while node is not None:
        node = node.left
        d += 1
    return d


def check_perfect_binary_tree(root, depth, level=0):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return depth == level + 1

    if root.left is None or root.right is None:
        return False

    return check_perfect_binary_tree(root.left, depth, level + 1) and check_perfect_binary_tree(root.right, depth,
                                                                                                level + 1)


def level_order_travesal(root):
    q = deque()
    q.append(root)
    while len(q) != 0:
        root = q.popleft()
        print(root.data, end=" ")
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        arr.pop()
        root = None
        root = insert_nodes(arr, root, 0, len(arr))
        depth = get_depth(root)
        # level_order_travesal(root)
        if check_perfect_binary_tree(root, depth):
            print("True")
        else:
            print("False")
