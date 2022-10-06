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


def construct_binary_search_tree_using_preorder_traversal(preorder, p_index=0, mini=float("-inf"), maxi=float("+inf")):
    if p_index == len(preorder):
        return None, p_index

    val = preorder[p_index]
    if val < mini or val > maxi:
        return None, p_index

    root = Node(val)
    p_index += 1

    root.left, p_index = construct_binary_search_tree_using_preorder_traversal(preorder, p_index, mini, val - 1)
    root.right, p_index = construct_binary_search_tree_using_preorder_traversal(preorder, p_index, val + 1, maxi)
    return root, p_index


def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    preorder = list(map(int, input().split()))
    root = construct_binary_search_tree_using_preorder_traversal(preorder)[0]
    postorder_traversal(root)
