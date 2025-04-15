# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# https://www.youtube.com/watch?v=PwMVNSJ5SLI




# Using Floyd Warshall - O(n^3)

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float("inf") or dist[k][j] == float("inf"):
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        min_count = n + 1
        city = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_count:
                min_count = count
                city = i
        return city


# Using Dijkstra alogo

# Dijkstra using a min-heap (priority queue) has complexity:

# O(E log V) using a binary heap (heapq in Python)

# In the worst case, for a dense graph:

# E ≈ n² (maximum edges in an undirected graph)

# So, O(n² log n) per Dijkstra

# 🔁 We run Dijkstra for all n cities:
# ✅ Total Time Complexity:
# O(n × (n² log n)) = O(n² log n) for sparse graphs
# O(n³ log n) for dense graphs

# But in most practical cases where edges are sparse, the Dijkstra version is faster than Floyd-Warshall.


import heapq

class Solution1:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(start: int) -> list[int]:
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]  # (distance, node)

            while heap:
                current_dist, u = heapq.heappop(heap)
                if current_dist > dist[u]:
                    continue
                for v, weight in graph[u]:
                    if dist[v] > current_dist + weight:
                        dist[v] = current_dist + weight
                        heapq.heappush(heap, (dist[v], v))
            return dist

        min_reachable = n + 1
        city = -1

        for i in range(n):
            distances = dijkstra(i)
            count = sum(1 for j in range(n) if i != j and distances[j] <= distanceThreshold)
            if count <= min_reachable:
                min_reachable = count
                city = i

        return city
