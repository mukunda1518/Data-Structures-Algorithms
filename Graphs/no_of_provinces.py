# https://leetcode.com/problems/number-of-provinces/description/?envType=problem-list-v2&envId=union-find

# https://www.youtube.com/watch?v=ZGr5nX-Gi6Y



class Solution:


    def find_ultimate_parent(self, node: int):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u: int, v: int):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        self.size = [1] * n
        self.parent = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and j != i:
                    self.union_by_size(i, j)
        res = 0
        for i in range(n):
            if self.find_ultimate_parent(i) == i:
                res += 1
        return res




        ## This is for adjacency list
        # We have to convert adjacency list to adjacnecy matrix
        # TC - O(n + 2e)
        n = len(isConnected)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and j != i:
                    graph[i].append(j)
        
        def dfs(city):
            visited.add(city)
            for neighbour in graph[city]:
                if neighbour not in visited:
                    dfs(neighbour)
    
        visited = set()
        provinces = 0
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                provinces += 1
        return provinces


        ### This if for adjacency matrix
        # TC - O(n^2)
        def dfs(city):
            visited.add(city)
            for neighbour, connected in enumerate(isConnected[city]):
                if neighbour not in visited and connected:
                    dfs(neighbour)

        visited = set()
        provinces = 0
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                provinces += 1
        return provinces