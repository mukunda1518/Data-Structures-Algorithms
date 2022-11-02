# Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_binary_tree_approach1(pre_order, in_order):
    if len(pre_order) <= 0 and len(in_order) <= 0:
        return

    data = pre_order[0]
    root = Node(data)  # Creating root node for every subtree
    root_index = in_order.index(data)
    # Recursively construct the left subtree
    root.left = build_binary_tree_approach1(pre_order[1:root_index + 1], in_order[0:root_index])
    # Recursively construct the right subtree
    root.right = build_binary_tree_approach1(pre_order[root_index + 1:], in_order[root_index + 1:])
    return root


def build_binary_tree_by_using_hash_map(start, end, pre_order, in_order, in_order_map, preorder_index):
    if start > end:
        return None, preorder_index
    root = Node(pre_order[preorder_index])
    index = in_order_map[root.data]
    preorder_index += 1
    root.left, preorder_index = build_binary_tree_by_using_hash_map(start, index - 1, pre_order, in_order, in_order_map,
                                                                    preorder_index)
    root.right, preorder_index = build_binary_tree_by_using_hash_map(index + 1, end, pre_order, in_order, in_order_map,
                                                                     preorder_index)
    return root, preorder_index


def build_binary_tree_approach2(pre_order, in_order):
    in_order_map = {}
    for i, val in enumerate(in_order):
        in_order_map[val] = i
    preorder_index = 0
    return build_binary_tree_by_using_hash_map(
        0, len(pre_order) - 1, pre_order, in_order, in_order_map, preorder_index
    )[0]


def build_binary_tree_approach3(pre_order, in_order):
    in_order_map = {}
    for i, val in enumerate(in_order):
        in_order_map[val] = i
    len_ = len(pre_order)

    def build_binary_tree(preorder, pre_s, pre_e, inorder, in_s, in_e, in_map):
        if pre_s > pre_e or in_s > in_e:
            return None
        node = Node(preorder[pre_s])
        n_index = in_map[root.data] # node index

        nums_left = n_index - in_s

        node.left = build_binary_tree(preorder, pre_s + 1, pre_s + nums_left, inorder, in_s, n_index - 1, in_map)
        node.right = build_binary_tree(preorder, pre_s + nums_left + 1, pre_e, inorder, n_index + 1, in_e, in_map)
        return root
    return build_binary_tree(pre_order, 0, len_ - 1, in_order, 0, len_ - 1, in_order_map)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    pre_order = list(map(int, input().split()))  # preorder 8 4 7 3 15 10
    in_order = list(map(int, input().split()))   # in order 7 4 3 8 10 15
    root = None
    # root = build_binary_tree_approach1(pre_order, in_order)
    root = build_binary_tree_approach2(pre_order, in_order)
    post_order(root)  # 7 3 4 10 15 8

