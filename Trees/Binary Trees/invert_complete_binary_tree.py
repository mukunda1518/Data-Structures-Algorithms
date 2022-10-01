# Leetcode: https://leetcode.com/problems/invert-binary-tree/description/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_complete_binary_tree(root, i, arr):
    if i < len(arr):
        root = Node(arr[i])
        root.left = build_complete_binary_tree(root.left, 2 * i + 1, arr)
        root.right = build_complete_binary_tree(root.right, 2 * i + 2, arr)
    return root


def invert_complete_binary_tree(root):
    if not root:
        return None
    temp = root.left
    root.left = invert_complete_binary_tree(root.right)
    root.right = invert_complete_binary_tree(temp)
    return root


def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    root = None
    root = build_complete_binary_tree(root, 0, arr)
    root = invert_complete_binary_tree(root)
    postorder_traversal(root)

