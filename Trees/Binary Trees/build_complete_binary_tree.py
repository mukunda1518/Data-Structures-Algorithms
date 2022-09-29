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

def preorder_travesal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_travesal(root.left)
    preorder_travesal(root.right)
        

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    root = None
    root = build_complete_binary_tree(root, 0, arr)
    preorder_travesal(root)

    