# Leetcode: https://leetcode.com/problems/rotting-oranges/description/

# https://www.youtube.com/watch?v=yf3oUhkvqA0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=10


# Time Complexity - O(n * m)

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = []
        queue = deque()
        for i in range(n):
            vis_r = []
            for j in range(m):
                if grid[i][j] == 2:
                    vis_r.append(2)
                    queue.append(((i, j), 0))
                else:
                    vis_r.append(0)
            vis.append(vis_r)
        
        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            (row, col), t = queue.popleft()
            for r, c in directions:
                nrow = row + r
                ncol = col + c
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and vis[nrow][ncol] != 2:
                    vis[nrow][ncol] = 2
                    queue.append(((nrow, ncol), t + 1))
            time = max(time, t)

        for i in range(n):
            for j in range(m):
                if vis[i][j] != 2 and grid[i][j] == 1:
                    return -1
        return time 

        