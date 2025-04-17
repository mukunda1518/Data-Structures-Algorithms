# https://leetcode.com/problems/minimum-falling-path-sum/

# https://www.youtube.com/watch?v=N_aJ5qQbYA0


class Solution:

    # TC: n * 3^n
    # SC: O(n)
    def min_path_recurr(self, i, j, matrix, n):
        if j < 0 or j >= n:
            return float("inf")
        if i == 0:
            return matrix[i][j]
        
        ld = matrix[i][j] + self.min_path_recurr(i - 1, j - 1, matrix, n)
        up = matrix[i][j] + self.min_path_recurr(i - 1, j, matrix, n)
        rd = matrix[i][j] + self.min_path_recurr(i - 1, j + 1, matrix, n)
        return min(ld, up, rd)
    
    # TC: n * n
    # SC: O(n * m) + O(n)
    def min_path_meomo(self, i, j, dp, matrix, n):
        if j < 0 or j >= n:
            return float("inf")
        if i == 0:
            return matrix[i][j]
        if dp[i][j] != float("inf"):
            return dp[i][j]
        
        ld = matrix[i][j] + self.min_path_meomo(i - 1, j - 1, dp, matrix, n)
        up = matrix[i][j] + self.min_path_meomo(i - 1, j, dp, matrix, n)
        rd = matrix[i][j] + self.min_path_meomo(i - 1, j + 1, dp, matrix, n)
        dp[i][j] = min(ld, up, rd)
        return dp[i][j]

    # TC: n * n
    # SC: O(n * m) 
    def min_path_tabulation(self, m, n, matrix):
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0] = matrix[0]
        for i in range(1, m):
            for j in range(n):
                ld = matrix[i][j] + dp[i-1][j-1] if j > 0 else float("inf")
                up = matrix[i][j] + dp[i-1][j]
                rd = matrix[i][j] + dp[i-1][j+1] if j + 1 < n else float("inf")
                dp[i][j] = min(ld, up, rd)
        return min(dp[0])

    # TC: n * n
    # SC: O(n) 
    def min_path_tabulation(self, m, n, matrix):
        prev_row = matrix[0]
        for i in range(1, m):
            curr_row = [float("inf")] * n
            for j in range(n):
                ld = matrix[i][j] + prev_row[j-1] if j > 0 else float("inf")
                up = matrix[i][j] + prev_row[j]
                rd = matrix[i][j] + prev_row[j+1] if j + 1 < n else float("inf")
                curr_row[j] = min(ld, up, rd)
            prev_row = curr_row
        return min(prev_row)

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[float("inf")] * n for _ in range(m)]
        min_path = float("inf")
        for j in range(n):
            min_path = min(min_path, self.min_path_meomo(m-1, j, dp, matrix, n))
        return min_path

