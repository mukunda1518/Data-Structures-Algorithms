# https://leetcode.com/problems/triangle/

# https://www.youtube.com/watch?v=SrP-PiLSYC0


class Solution:

    # Time Complexity - O(2^(n*(n+1)//2)) - O(2^(n*n))
    # Space Complexity - O(n)
    def min_recurr(self, i, j, triangle, n):
        if i == n - 1:
            return triangle[i][j]
        down = triangle[i][j] + self.min_recurr(i + 1, j , triangle, n)
        down_left = triangle[i][j] + self.min_recurr(i + 1, j + 1, triangle, n)
        return min(down, down_left)

    # Memoization - TC - O(n*n) , SC - O(n*n)
    def min_recurr(self, i, j, dp, triangle, n):
        if i == n - 1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        down = triangle[i][j] + self.min_recurr(i + 1, j, dp, triangle, n)
        down_left = triangle[i][j] + self.min_recurr(i + 1, j + 1, dp, triangle, n)
        dp[i][j] = min(down, down_left)
        return dp[i][j]

    # Time Complexity = O(n*n)
    # Space Complexity = (n*n) - no recurssion stack space
    def min_tabulation(self, n, triangle):
        dp = [[-1] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                if i == n - 1:
                    dp[i][j] = triangle[i][j]
                    continue
                down = triangle[i][j] + dp[i+1][j]
                down_left = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down, down_left)
        return dp[0][0]
    
    # Time Complexity = O(n*n)
    # Space Complexity = (n*n) - no recurssion stack space
    def min_tabulation_space(self, n, triangle):
        prev_row = triangle[-1]
        for i in range(n-2, -1, -1):
            curr_row = [0] * (i + 1)
            for j in range(i+1):
                down = triangle[i][j] + prev_row[j]
                down_left = triangle[i][j] + prev_row[j+1]
                curr_row[j] = min(down, down_left)
            prev_row = curr_row
        return prev_row[0]

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)

        return self.min_tabulation_space(n, triangle)

        return self.min_tabulation(n, triangle)

        dp = [[-1] * n for _ in range(n)]
        return self.min_recurr(0, 0, dp, triangle, n)
        return self.min_recurr(0, 0, triangle, n)
        