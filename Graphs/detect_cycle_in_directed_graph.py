# https://www.youtube.com/watch?v=9twcmtQj4DU


# TC - O(n + e)


class Solution:
    def dfs_check(self, node, vis, path_vis, graph):
        vis[node] = 1
        path_vis[node] = 1

        for n_node in graph[node]:
            if not vis[n_node]:
                if self.dfs_check(n_node, vis, path_vis, graph):
                    return True
            elif path_vis[n_node]:
                return True
        path_vis[node] = 0
        return False

    def detect_cycle(self, n: int, graph: list[list[int]]) -> list[int]:
        vis = [0 for _ in range(n)]
        path_vis = [0 for _ in range(n)]

        for i in range(n):
            if not vis[i]:
                if self.dfs_check(i, vis, path_vis, graph):
                    return True
        return False
    

class Solution1:
    def dfs_check(self, node, vis, graph):
        vis[node] = 1  # Mark as visiting

        for n_node in graph[node]:
            if vis[n_node] == 0:
                if self.dfs_check(n_node, vis, graph):
                    return True
            elif vis[n_node] == 1:
                # Cycle detected (back edge)
                return True

        vis[node] = 2  # Mark as fully visited
        return False

    def detect_cycle(self, n: int, graph: list[list[int]]) -> bool:
        vis = [0] * n

        for i in range(n):
            if vis[i] == 0:
                if self.dfs_check(i, vis, graph):
                    return True
        return False
