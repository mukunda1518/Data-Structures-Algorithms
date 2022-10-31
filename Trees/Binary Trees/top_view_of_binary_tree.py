# Leetcode: https://leetcode.com/discuss/general-discussion/1094690/views-and-traversal-of-binary-tree-important-topics-must-read
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




