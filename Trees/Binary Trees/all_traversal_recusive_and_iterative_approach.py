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


def level_order_traversal_iterative(root):
    q = deque()
    q.append(root)
    while len(q) != 0:
        root = q.popleft()
        print(root.data, end=" ")
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
    print()


def pre_order_traversal_recursive(root):
    if root is not None:
        print(root.data, end=" ")
        pre_order_traversal_recursive(root.left)
        pre_order_traversal_recursive(root.right)


def pre_order_traversal_iterative(root):
    stack = [root]
    while stack:
        root = stack.pop()
        print(root.data, end=" ")
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    print()


def in_order_traversal_recursive(root):
    if root is not None:
        in_order_traversal_recursive(root.left)
        print(root.data, end=" ")
        in_order_traversal_recursive(root.right)


def in_order_traversal_iterative(root):
    stack = []
    while root != None or stack:
        while(root):
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.data, end=" ")
        root = root.right
    print()


def post_order_traversal_recursive(root):
    if root is not None:
        post_order_traversal_recursive(root.left)
        post_order_traversal_recursive(root.right)
        print(root.data, end=" ")


def post_order_traversal_iterative(root):
    stack = []
    while True:

        while root:
            stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()

        if len(stack) == 0:
            print(root.data, end=" ")
            break

        if root.right == stack[-1]:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print(root.data, end=" ")
            root = None
    print()


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = None
    root = insert_nodes(arr, root, 0, len(arr))
    print("Level order traversal - Iterative")
    level_order_traversal_iterative(root)
    print("Pre order traversal - Iterative and Recursive")
    pre_order_traversal_iterative(root)
    pre_order_traversal_recursive(root)
    print()
    print("In order traversal - Iterative and Recursive")
    in_order_traversal_iterative(root)
    in_order_traversal_recursive(root)
    print()
    print("Post order traversal - Iterative and Recursive")
    post_order_traversal_iterative(root)
    post_order_traversal_recursive(root)






