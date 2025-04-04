# Leetcode: https://leetcode.com/problems/is-graph-bipartite/
# https://www.youtube.com/watch?v=KG5YFfR0j8A


# TC - O(n + 2e)

class Solution:

    def dfs(self, node, col, colors, graph):
        colors[node] = col
        for n_node in graph[node]:
            if colors[n_node] == -1:
                if self.dfs(n_node, 1 - col, colors, graph) is False:
                    return False
            elif colors[n_node] == col:
                return False
        return True

    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [ -1 for _ in range(n)]
        
        for i in range(n):
            if colors[i] == -1:
                if self.dfs(i, 0, colors, graph) is False:
                    return False
        return True
