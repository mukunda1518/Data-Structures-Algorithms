# Leetcode: https://leetcode.com/problems/number-of-islands/
# https://www.youtube.com/watch?v=muncqlKJrH0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=8


# Time Complexity = O(n^2) + O(n^2) * 4
# Space Complexity = O(n^2)


from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _ in range(n)]

        def bfs(i, j):
            vis[i][j] = 1
            queue = deque([(i, j)])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                row, col = queue.popleft()
                for d_row, d_col in directions:
                    nrow = d_row + row
                    ncol = d_col + col
                    if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == "1" and not vis[nrow][ncol]:
                        vis[nrow][ncol] = 1
                        queue.append((nrow, ncol))

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not vis[i][j]:
                    count += 1
                    bfs(i, j)
        return count
