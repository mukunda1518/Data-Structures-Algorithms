# Problem: https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1


class Solution:
    # Function to find all possible paths
    
    def solve(self, i, j, n, move, dirs, mat, visited, res, di, dj):
        if i == n - 1 and j == n - 1:
            res.append(move)
            return

        for k in range(len(dirs)):
            nexti = i + di[k]
            nextj = j + dj[k]
            if nexti >= 0 and nexti < n and nextj >= 0 and nextj < n and not visited[nexti][nextj] and mat[nexti][nextj] == 1:
                visited[nexti][nextj] = 1
                self.solve(nexti, nextj, n, move + dirs[k], dirs, mat, visited, res, di, dj)
                visited[nexti][nextj] = 0
    
    def findPath(self, mat):
        n = len(mat)
        di = [1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        move = ""
        dirs = "DLRU"
        res = []
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1
        self.solve(0, 0, n, move, dirs, mat, visited, res, di, dj)
        return res
