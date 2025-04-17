# Problem - https://www.geeksforgeeks.org/problems/chocolates-pickup/1
# https://www.youtube.com/watch?v=QGfn7JeXK54


class Solution:
    
    # Time Complexity - O(3^n * 3^n)
    # Space Complexity - O(n)
    def max_recurr(self, i, j1, j2, r, c, grid):
        if j1 < 0 or j2 < 0 or j1 >= c or j2 >= c:
            return 1e-8
        if i == r - 1:
            return grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
        
        max_val = 1e-8
        for dj1 in [-1, 0, +1]:
            for dj2 in [-1, 0, +1]:
                val = 0
                if j1 == j2:
                    val = grid[i][j1]
                else:
                    val = grid[i][j1] + grid[i][j2]
                val += self.max_recurr(i + 1, j1 + dj1, j2 + dj2, r, c, grid)
                max_val = max(max_val, val)
        return max_val
    
    # Time Complexity - O(n * m * m) * 9
    # Space Complexity - O(n * m * m) + O(n)
    def max_recurr_memo(self, i, j1, j2, r, c, grid, dp):
        if j1 < 0 or j2 < 0 or j1 >= c or j2 >= c:
            return 1e-8
        if i == r - 1:
            return grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        max_val = 1e-8
        for dj1 in [-1, 0, +1]:
            for dj2 in [-1, 0, +1]:
                val = 0
                if j1 == j2:
                    val = grid[i][j1]
                else:
                    val = grid[i][j1] + grid[i][j2]
                val += self.max_recurr_memo(i + 1, j1 + dj1, j2 + dj2, r, c, grid, dp)
                max_val = max(max_val, val)
        dp[i][j1][j2] = max_val
        return dp[i][j1][j2]
                

    
    def solve(self, n, m, grid):
        # Code here
        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]
        print(dp)
        return self.max_recurr_memo(0, 0, m-1, n, m, grid, dp)

