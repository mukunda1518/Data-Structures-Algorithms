# Leetcode: https://leetcode.com/problems/boundary-of-binary-tree/
# https://www.youtube.com/watch?v=0ca1nvR0be4

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree(arr):
    if not arr:
        return
    val = arr.pop()

    if val == "#":
        return

    root = Node(val)
    root.left = create_tree(arr)
    root.right = create_tree(arr)
    return root


def left_boundary(root, result):
    if root is None or (root.left is None and root.right is None):
        return
    result.append(root.data)
    if root.left:
        left_boundary(root.left, result)
    else:
        left_boundary(root.right, result)


def leaves(root, result):
    if root is None:
        return
    if root.left is None and root.right is None:
        result.append(root.data)
        return
    leaves(root.left, result)
    leaves(root.right, result)


def right_boundary(root, result):
    if root is None or (root.left is None and root.right is None):
        return
    if root.right:
        right_boundary(root.right, result)
    else:
        right_boundary(root.left, result)
    result.append(root.data)


def build_boundaries_of_binary_tree(root):
    result = []
    if root is None:
        return result
    if root.left is None and root.right is None:
        return [root.data]

    result.append(root.data)
    left_boundary(root.left, result)
    leaves(root, result)
    right_boundary(root.right, result)
    return result


if __name__ == "__main__":
    arr = input().split()  # Pre-order  Here # means null, input: 5 3 8 # # # 7 9 # # #   output: 5 3 8 9 7
    arr = arr[::-1]
    root = create_tree(arr)
    res = build_boundaries_of_binary_tree(root)
    print(*res)
