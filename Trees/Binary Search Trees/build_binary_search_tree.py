class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_binary_search_tree(arr):
    root = None
    for num in arr:
        root = insert_node(root, num)
    return root


def insert_node(root, num):
    if root is None:
        return Node(num)
    if num < root.data:
        root.left = insert_node(root.left, num)
    else:
        root.right = insert_node(root.right, num)
    return root


def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    # First num in the list is root
    arr = list(map(int, input().split()))
    root = build_binary_search_tree(arr)
    postorder_traversal(root)
