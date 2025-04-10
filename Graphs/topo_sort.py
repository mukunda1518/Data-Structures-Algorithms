# https://www.youtube.com/watch?v=5lZ0iJMrUMk



class Solution:
    
    def dfs(self, node, vis, stack, adj):
        vis[node] = 1
        for n_node in adj[node]:
            if not vis[n_node]:
                self.dfs(n_node, vis, stack, adj)
        stack.append(node)
    
    def topoSort(self, V, edges):
        # Code here
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        vis = [0] * V
        stack = []
        
        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, stack, adj)
        return stack[::-1]
