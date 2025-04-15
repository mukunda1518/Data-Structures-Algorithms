# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

# https://www.youtube.com/watch?v=0vVofAhAYjc



# Time Complexity - O(V * E)




class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''
    def bellmanFord(self, V, edges, src):
        #code here
        INF = 10**8
        dist = [INF] * V
        dist[src] = 0
        for i in range(V-1):
            for u, v, wt in edges:
                if dist[u] != INF and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        
        # For nth relaxation to negative cycles
        for u, v, wt in edges:
            if dist[u] != INF and dist[u] + wt < dist[v]:
                return [-1]

        return dist