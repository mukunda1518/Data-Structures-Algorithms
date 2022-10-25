
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


def all_traversals(root):
    stack = [(root, 1)]   # Stores node and counter
    # Counter - 1 - Preorder
    # Counter - 2 - Inorder
    # Counter - 3 - Postorder
    preorder = []
    inorder = []
    postorder = []

    while len(stack) != 0:
        node, counter = stack.pop()
        if counter == 1:
            preorder.append(node.data)
            counter += 1
            stack.append((node, counter))
            if node.left:
                stack.append((node.left, 1))
        elif counter == 2:
            inorder.append(node.data)
            counter += 1
            stack.append((node, counter))
            if node.right:
                stack.append((node.right, 1))
        elif counter == 3:
            postorder.append(node.data)

    print("Preorder: {}".format(preorder))
    print("Inorder: {}".format(inorder))
    print("Postorder: {}".format(postorder))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = None
    root = insert_nodes(arr, root, 0, len(arr))
    all_traversals(root)