# leetcode : https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# https://www.youtube.com/watch?v=Hr5cWUld4vU
from collections import deque
import sys

int_max = sys.maxsize

queue = deque()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(arr, root):
    for i in range(len(arr)):
        if arr[i] != "null":
            root = insert_node(arr[i], root)
        else:
            root = insert_node(int_max, root)
    root = remove_null_nodes(root)
    return root


def insert_node(data, root):
    new_node = Node(data)
    if len(queue) != 0:
        temp = queue[0]

    if root is None:
        root = new_node
    elif temp.left == None:
        temp.left = new_node
    elif temp.right == None:
        temp.right = new_node
        queue.popleft()

    if data != int_max:
        queue.append(new_node)
    return root

def remove_null_nodes(root):
    if root is None or root.data == int_max:
        return None
    root.left = remove_null_nodes(root.left)
    root.right = remove_null_nodes(root.right)
    return root

def find_max_sum_path1(root):
    max_sum = float("-inf")
    def find_max_sum_path(root):
        if not root:
            return 0
        left_max = find_max_sum_path(root.left)
        right_max = find_max_sum_path(root.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)
        nonlocal max_sum
        max_sum = max(max_sum, int(root.data) + left_max + right_max)
        return int(root.data) + max(left_max, right_max)
    find_max_sum_path(root)
    return max_sum


if __name__ == "__main__":
    arr = [x for x in input().split()]
    root = None
    root = build_tree(arr, root)
    print(find_max_sum_path1(root))
        


from typing import Optional

# Which handles negative values also

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")]

        def dfs(node):
            if node is None:
                return 0
            
            lmax = dfs(node.left)
            rmax = dfs(node.right)

            single_path_sum = max(node.val, node.val + lmax, node.val + rmax)
            max_sum[0] = max(max_sum[0], single_path_sum, node.val + lmax + rmax)
            return single_path_sum

        dfs(root)
        return max_sum[0]


class Solution1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return (float("-inf"), 0)
            
            lmax, lsingle = dfs(node.left)
            rmax, rsingle = dfs(node.right)

            single_path_sum = max(node.val, node.val + lsingle, node.val + rsingle)
            max_sum = max(lmax, rmax, single_path_sum, node.val + lsingle + rsingle)
            return (max_sum, single_path_sum)

        return dfs(root)[0]



        