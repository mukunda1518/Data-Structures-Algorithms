# Problem:  https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

# You are given an undirected graph consisting of v vertices and a list of edges, along with an integer m. Your task is to determine whether it is possible to color the graph using at most m different colors such that no two adjacent vertices share the same color. Return true if the graph can be colored with at most m colors, otherwise return false.

# Note: The graph is indexed with 0-based indexing.


# Input: v = 4, edges[] = [(0,1),(1,2),(2,3),(3,0),(0,2)], m = 3
# Output: true
# Explanation: It is possible to color the given graph using 3 colors, for example, one of the possible ways vertices can be colored as follows:
# Vertex 0: Color 3
# Vertex 1: Color 2
# Vertex 2: Color 1
# Vertex 3: Color 2



class Solution:
    
    def is_safe(self, idx, edges, i, colors):
        for edge in edges:
            if (edge[0] == idx and colors[edge[1]] == i) or (edge[1] == idx and colors[edge[0]] == i):
                return False
        return True
    
    def solve(self, idx, v, edges, m, colors):
        if idx == v:
            return True
        for i in range(1, m + 1):
            if self.is_safe(idx, edges, i, colors):
                colors[idx] = i
                if self.solve(idx+1, v, edges, m, colors):
                    return True
                else:
                    colors[idx] = 0
        return False
                
    
    def graphColoring(self, v, edges, m):
        colors = [0] * v
        return self.solve(0, v, edges, m, colors)

