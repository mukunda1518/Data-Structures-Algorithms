# https://www.geeksforgeeks.org/problems/binary-tree-representation/1


from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def createTree(self, root, l):
        queue = deque([root])
        i = 1
        n = len(l)
        while i < n:
            curr = queue.popleft()
            if i < n:
                curr.left = Node(l[i])
                queue.append(curr.left)
            i += 1
            if i < n:
                curr.right = Node(l[i])
                queue.append(curr.right)
            i += 1