# Problem: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# https://www.youtube.com/watch?v=Qzf1a--rhp8



class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        
        n = len(adj)
        res = []
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            res.append(node)
            for n_node in adj[node]:
                if not visited[n_node]:
                    dfs(n_node)
        dfs(0)
        return res