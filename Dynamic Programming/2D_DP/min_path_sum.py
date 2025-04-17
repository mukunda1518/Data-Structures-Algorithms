# https://leetcode.com/problems/minimum-path-sum/

# https://www.youtube.com/watch?v=_rgTlyky1uQ



class Solution:

    # Time complexity = O(2^(n * m))
    def min_path_sum_recurssion(self, i, j, matrix):
        if i == 0 and j == 0:
            return matrix[i][j]
        if i < 0 or j < 0:
            return float("inf")

        up = matrix[i][j] + self.min_path_sum_recurssion(i-1, j, matrix)
        down = matrix[i][j] + self.min_path_sum_recurssion(i, j-1, matrix)
        return min(up, down)
    
    # Memoization using DP - O(n * m)
    def min_path_sum_memo(self, i, j, matrix, dp):
        if i == 0 and j == 0:
            return matrix[i][j]
        if i < 0 or j < 0:
            return float("inf")
        if dp[i][j] != -1:
            return dp[i][j]

        up = matrix[i][j] + self.min_path_sum_memo(i-1, j, matrix, dp)
        down = matrix[i][j] + self.min_path_sum_memo(i, j-1, matrix, dp)
        dp[i][j] = min(up, down)
        return dp[i][j]

    # Tabulation using DP - O(n * m)
    # Space = O(n * m)
    def unique_paths_tabu(self, m, n, matrix):
        dp = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = matrix[0][0]
                    continue
                up = matrix[i][j] + dp[i-1][j] if i > 0 else float("inf")
                left = matrix[i][j] + dp[i][j-1] if j > 0 else float("inf")
                dp[i][j] = min(up, left)
        return dp[m-1][n-1]

    # Tabulation using DP space optimized - O(n * m)
    # Space = O(n)
    def unique_paths_tabu_space(self, m, n, matrix):
        prev_row = [0] * n
        for i in range(m):
            curr_row = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr_row[j] = matrix[i][j]
                    continue
                up = matrix[i][j] + prev_row[j] if i > 0 else float("inf")
                left = matrix[i][j] + curr_row[j-1] if j > 0 else float("inf")
                curr_row[j] = min(up, left)
            prev_row = curr_row
        return prev_row[-1]

    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.min_path_sum_recurssion(m-1, n-1, grid)

        dp = [[-1] * n for _ in range(m)]
        self.min_path_sum_memo(m-1, n-1, grid, dp)

        self.unique_paths_tabu(m, n, grid)

        return self.unique_paths_tabu_space(m, n, grid)



