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


def get_inorder_traversal(root, tree_elemnts):
    if root is None:
        return
    get_inorder_traversal(root.left, tree_elemnts)
    tree_elemnts.append(root.data)
    get_inorder_traversal(root.right, tree_elemnts)


def get_pairs_count(tree1_elemnts, tree2_elemnts, k):
    i = 0
    j = len(tree2_elemnts) - 1
    tree1_len = len(tree1_elemnts)
    count = 0
    while j >= 0 and i < tree1_len:
        if tree1_elemnts[i] + tree2_elemnts[j] > k:
            count += tree1_len - i
            j -= 1
        else:
            i += 1
    return count


if __name__ == "__main__":
    k = int(input())
    arr1 = input().split()[0:-1]
    arr2 = input().split()[0:-1]
    root1 = build_bst(arr1)
    root2 = build_bst(arr2)
    tree1_elemnts = []
    tree2_elemnts = []
    get_inorder_traversal(root1, tree1_elemnts)
    get_inorder_traversal(root2, tree2_elemnts)
    print(get_pairs_count(tree1_elemnts, tree2_elemnts, k))
