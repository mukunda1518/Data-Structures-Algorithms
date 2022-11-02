# Leetcode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        dq = deque()
        dq.append(root)
        ser = ""
        while dq:
            node = dq.popleft()
            if node is None:
                ser +=  "#" + " "
            else:
                ser += str(node.val) + " "
                dq.append(node.left)
                dq.append(node.right)
        return ser.rstrip()



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        des = data.split(" ")
        len_ = len(des)
        root = TreeNode(int(des[0]))
        dq = deque()
        dq.append(root)
        i = 1
        while i < len_ - 1:
            node = dq.popleft()
            if des[i] != "#":
                new_node = TreeNode(int(des[i]))
                node.left = new_node
                dq.append(new_node)
            i += 1
            if des[i] != "#":
                new_node = TreeNode(int(des[i]))
                node.right = new_node
                dq.append(new_node)
            i += 1

        return root




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))