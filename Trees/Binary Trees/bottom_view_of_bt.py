# https://takeuforward.org/plus/dsa/problems/bottom-view-of-bt
# https://www.youtube.com/watch?v=0FtVY6I4pB8



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        # Map to store the latest node at each vertical
        vertical_map = dict()

        # Queue for BFS: (node, vertical)
        queue = deque([(root, 0)])

        while queue:
            node, vertical = queue.popleft()
            # Always overwrite: bottom-most node at each vertical
            vertical_map[vertical] = node.val

            if node.left:
                queue.append((node.left, vertical - 1))
            if node.right:
                queue.append((node.right, vertical + 1))

        # Return results from leftmost to rightmost vertical
        return [vertical_map[v] for v in sorted(vertical_map)]
