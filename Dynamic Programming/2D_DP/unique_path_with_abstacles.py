# https://leetcode.com/problems/unique-paths-ii/description/

# https://www.youtube.com/watch?v=TmhpgXScLyY



class Solution:

    # Time complexity = O(2^(n * m))
    def unique_paths_recurssion(self, i, j, matrix):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        if matrix[i][j] == 1:
            return 0

        up = self.unique_paths_recurssion(i-1, j, matrix)
        down = self.unique_paths_recurssion(i, j-1, matrix)
        return up + down
    
    # Memoization using DP - O(n * m)
    def unique_paths_memo(self, i, j, matrix, dp):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        if matrix[i][j] == 1:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        up = self.unique_paths_memo(i-1, j, matrix, dp)
        down = self.unique_paths_memo(i, j-1, matrix, dp)
        dp[i][j] = up + down
        return dp[i][j]

    # Tabulation using DP - O(n * m)
    # Space = O(n * m)
    def unique_paths_tabu(self, m, n, matrix):
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                dp[i][j] = up + left
        return dp[m-1][n-1]

    # Tabulation using DP space optimized - O(n * m)
    # Space = O(n)
    def unique_paths_tabu_space(self, m, n, matrix):
        prev = [0] * n
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if matrix[i][j] == 1:
                    temp[j] = 0
                    continue
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                up = prev[j]
                left = temp[j-1] if j > 0 else 0
                temp[j] = up + left
            prev = temp
        return prev[-1]

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        # return self.unique_paths_recurssion(m-1, n-1, obstacleGrid)

        # dp = [[-1] * n for _ in range(m)]
        # return self.unique_paths_memo(m-1, n-1, obstacleGrid, dp)
        
        # return self.unique_paths_tabu(m, n, obstacleGrid)

        return self.unique_paths_tabu_space(m, n, obstacleGrid)

