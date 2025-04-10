# https://leetcode.com/problems/course-schedule-ii/

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            indgree[u] += 1

        queue = deque()
        for i in range(numCourses):
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
  
        return topo if len(topo) == numCourses else [] 
