class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_inorder_successor(root, val):
    successor = None

    while root:

        if root.data > val:
            successor = root
            root = root.left
        elif root.data <= val:
            root = root.right
    return successor


def get_inorder_predecessor(root, val):
    predecessor = None

    while root:

        if root.val < val:
            predecessor = root
            root = root.right
        elif root.val >= val:
            root = root.left

    return predecessor

