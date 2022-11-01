# Leetcode: https://leetcode.com/discuss/general-discussion/1094690/views-and-traversal-of-binary-tree-important-topics-must-read
# https://www.youtube.com/watch?v=Et9OCDNvJ78&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=23


from collections import deque, OrderedDict


class Node:
    def __int__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_top_view_of_tree(root):
    map_ = OrderedDict()
    dq = deque()
    dq.append((root, 0))

    while not dq:
        node, vh = dq.popleft()  # vh - vertical height
        if vh not in map_:
            map_[vh] = node.data
        if node.left:
            dq.append((node.left, vh - 1))
        if node.right:
            dq.append((node.right, vh + 1))
    top_view_dq = deque()
    keys = map_.keys()
    for i, key in enumerate(keys):
        if abs(i) % 2 == 0:
            top_view_dq.append(map_[key])
        else:
            top_view_dq.appendleft(map_[key])
    print(top_view_dq)


def get_bottom_view_of_tree(root):
    map_ = OrderedDict()
    dq = deque()
    dq.append((root, 0))

    while not dq:
        node, vh = dq.popleft()  # vh - vertical height
        map_[vh] = node.data
        if node.left:
            dq.append((node.left, vh - 1))
        if node.right:
            dq.append((node.right, vh + 1))
    top_view_dq = deque()
    keys = map_.keys()
    for i, key in enumerate(keys):
        if abs(i) % 2 == 0:
            top_view_dq.append(map_[key])
        else:
            top_view_dq.appendleft(map_[key])
    print(top_view_dq)


def get_right_side_view(root):
    rs_view_nums = []  # Right Side view nums
    map_ = {}  # Contains Right side view nums

    def right_side_view(root, level=0):
        if root is None:
            return

        if level == len(rs_view_nums):   # can store this way also
            rs_view_nums.append(root.data)

        if level not in map_:   # can store this way also
            map_[level] = root.data

        if root.right:
            right_side_view(root.right, level + 1)

        if root.left:
            right_side_view(root.left, level + 1)

    right_side_view(root)


def get_left_side_view(root):
    ls_view_nums = []  # Right Side view nums
    map_ = {}  # Contains Right side view nums

    def left_side_view(root, level=0):
        if root is None:
            return

        if level == len(ls_view_nums):   # can store this way also
            ls_view_nums.append(root.data)

        if level not in map_:   # can store this way also
            map_[level] = root.data

        if root.left:
            left_side_view(root.left, level + 1)

        if root.right:
            left_side_view(root.right, level + 1)

    get_left_side_view(root)



