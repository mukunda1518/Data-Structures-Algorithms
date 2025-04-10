# Problem: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
# https://www.youtube.com/watch?v=ZUFQfFaU-8U&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=18

# Input: V = 4, E = 2, edges = [[0,1,2], [0,2,1]]
# Output: [0, 2, 1, -1]
# Explanation: Shortest path from 0 to 1 is 0->1 with edge weight 2. Shortest path from 0 to 2 is 0->2 with edge weight 1. There is no way we can reach 3, so it's -1 for 3.



from typing import List
from collections import defaultdict


class Solution:
    
    def topo_sort(self, node, stack, vis, graph):
        vis[node] = True
        for n, _ in graph[node]:
            if not vis[n]:
                self.topo_sort(n, stack, vis, graph)
        stack.append(node)

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, wt in edges:
            graph[u].append((v, wt))
        
        # Step 2: Topological sort using DFS
        stack = []
        vis = [False] * V
        for i in range(V):
            if not vis[i]:
                self.topo_sort(i, stack, vis, graph)
        
        # Step 3: Initialize distances
        dist = [float("inf")] * V
        dist[0] = 0 # distance to source is 0
        
        while stack:
            node = stack.pop()
            if dist[node] != float("inf"):
                for v, wt in graph[node]:
                    if dist[node] + wt < dist[v]:
                        dist[v] = dist[node] + wt

        # Step 5: Convert unreachable distances to -1
        return [-1 if d == float("inf")  else d for d in dist]
        
    