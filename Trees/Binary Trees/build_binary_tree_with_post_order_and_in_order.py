class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_binary_tree_by_using_hash_map(
        start, end, post_order, in_order, in_order_map, postorder_index
):
    if start > end:
        return None, postorder_index
    root = Node(post_order[postorder_index])
    index = in_order_map[root.data]
    postorder_index -= 1
    root.right, postorder_index = build_binary_tree_by_using_hash_map(
        index + 1, end, post_order, in_order, in_order_map, postorder_index
    )
    root.left, postorder_index = build_binary_tree_by_using_hash_map(
        start, index - 1, post_order, in_order, in_order_map, postorder_index
    )

    return root, postorder_index


def build_binary_tree(i_s, i_e, in_order, p_s, p_e, post_order, in_order_map):
    if i_s > i_e or p_s > p_e:
        return None

    root = Node(post_order[p_e])
    index = in_order_map[root.data]
    remain_nums = index - i_s
    root.left = build_binary_tree(i_s, index - 1, in_order, p_s, p_s + remain_nums - 1, post_order, in_order_map)
    root.right = build_binary_tree(index + 1, i_e, in_order, p_s + remain_nums, p_e - 1, post_order, in_order_map)
    return root


def pre_order(root):
    if root is None:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)


if __name__ == "__main__":
    in_order = list(map(int, input().split()))
    in_order.pop()
    post_order = list(map(int, input().split()))
    post_order.pop()
    len_ = len(in_order)
    root = None
    in_order_map = {}
    for i, val in enumerate(in_order):
        in_order_map[val] = i
    root = build_binary_tree(0, len_ - 1, in_order, 0, len_ - 1, post_order, in_order_map)
    pre_order(root)

