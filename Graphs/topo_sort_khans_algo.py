# https://www.youtube.com/watch?v=73sneFXuTEg&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=22

from collections import deque


# TC = O(V + E)

class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        adj = [[] for _ in range(V)]
        indgree = [0] * V

        for u, v in edges:
            adj[u].append(v)
            indgree[v] += 1
            
        queue = deque()
        for i in range(V):
            if indgree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)
            for n_node in adj[node]:
                indgree[n_node] -= 1
                if indgree[n_node] == 0:
                    queue.append(n_node)
  
        return topo
