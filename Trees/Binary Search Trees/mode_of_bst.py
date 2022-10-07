# Leetcode: https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

from collections import deque
import sys

int_max = sys.maxsize


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(arr):
    Q = deque()
    root = Node(int(arr[0]))
    Q.append(root)
    insert_nodes(Q, arr, 1)
    return root


def insert_nodes(Q, arr, index):
    while 1:
        if not Q:
            break
        node = Q.popleft()
        if index < len(arr):
            if arr[index] != "null":
                node.left = Node(int(arr[index]))
                Q.append(node.left)
            else:
                node.left = None
            index += 1
        if index < len(arr):
            if arr[index] != "null":
                node.right = Node(int(arr[index]))
                Q.append(node.right)
            else:
                node.right = None
            index += 1


class Solution:
    def __init__(self):
        self.prev = None
        self.result = None
        self.curr_freq = 0
        self.max_freq = 0

    def find_mode(self, root):
        if root is None:
            return
        self.find_mode(root.left)
        self.curr_freq = 1 if root.data != self.prev else self.curr_freq + 1
        if self.curr_freq > self.max_freq:
            self.result = root.data
            self.max_freq = self.curr_freq
        self.prev = root.data
        self.find_mode(root.right)


if __name__ == "__main__":
    arr = input().split()
    root = build_tree(arr)
    mode = Solution()
    mode.find_mode(root)
    print(mode.result)
