

# Problem: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
# https://www.youtube.com/watch?v=C4gxoTaI71U&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=19

# Input: adj[][] = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], src=0
# Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]


from collections import deque

class Solution:
    def shortestPath(self, adj, src):
        # code here
        
        n = len(adj)
        dist = [float("inf")] * n
        dist[src] = 0
        
        queue = deque([src])
        
        while queue:
            node = queue.popleft()
            for neighbour in adj[node]:
                if dist[node] + 1 < dist[neighbour]:
                    dist[neighbour] = dist[node] + 1
                    queue.append(neighbour)

        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        return dist
