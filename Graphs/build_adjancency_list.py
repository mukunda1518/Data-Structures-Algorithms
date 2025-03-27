from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        graph = [ [] for _ in range(V)]
        for i in range(len(edges)):
            n1, n2 = edges[i]
            graph[n1].append(n2)
            graph[n2].append(n1)
        return graph
