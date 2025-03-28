# Probelm: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# https://www.youtube.com/watch?v=BPlrALf1LDU&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=11


# Time Complexity - O(n + 2e) + O(n)


##### BFS

from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    
    def detect_cycle(self, v, adj, vis):
        vis[v] = 1
        queue = deque()
        queue.append((v, -1))
        while queue:
            node, parent = queue.popleft()
            for adj_node in adj[node]:
                if not vis[adj_node]:
                    vis[adj_node] = 1
                    queue.append((adj_node, node))
                elif adj_node != parent:
                    return True
        return False
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [0] * V
        for i in range(V):
            if not vis[i]:
                if self.detect_cycle(i, adj, vis):
                    return 1
        return 0


##### DFS

class Solution1:
    #Function to detect cycle in an undirected graph.
    
    def detect_cycle(self, n, par, adj, vis):
        vis[n] = 1
        for adj_n in adj[n]:
            if not vis[adj_n]:
                if self.detect_cycle(adj_n, n, adj, vis):
                    return True
            elif adj_n != par:
                return True
        return False
                

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        vis = [0] * V

        for i in range(V):
            if not vis[i]:
                if self.detect_cycle(i, -1, adj, vis):
                    return 1
        return 0