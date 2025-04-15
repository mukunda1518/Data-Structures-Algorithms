# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

# https://www.youtube.com/watch?v=V6H1qAeB-l4&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=20



import heapq
from collections import defaultdict


# Time Complexity - O(E logV)

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # Since the graph is undirected
        
        # Distance array initialized to infinity
        dist = [float("inf")] * V
        dist[src] = 0
        
        min_heap = [(0, src)]
        
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            if curr_dist > dist[node]:
                continue # already processed and no need to process higher weight value
            for adj_node, weight in graph[node]:
                distance = curr_dist + weight
                if distance < dist[adj_node]:
                    dist[adj_node] = distance
                    heapq.heappush(min_heap, (distance, adj_node))
        return dist
        
        