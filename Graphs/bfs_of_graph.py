# Problem: https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
# https://www.youtube.com/watch?v=-tgVpUgsQ5k&feature=youtu.be


# Time Complexity - O(n) + O(2e)


from typing import List
from collections import deque
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        bfs = []
        queue = deque([0])
        visited = [False] * len(adj)
        visited[0] = True
        while queue:
            node = queue.popleft()
            bfs.append(node)
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True
        return bfs

