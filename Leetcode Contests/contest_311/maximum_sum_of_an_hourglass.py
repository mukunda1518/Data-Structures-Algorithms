# Leetcode: https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/


class Solution:
    def maxSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        max_sum = 0

        for i in range(m - 2):
            sum_ = 0
            for j in range(n - 2):
                # Top row
                sum_ = sum(grid[i][j:j + 3])
                # Bottom row
                sum_ += sum(grid[i + 2][j:j + 3])
                # Middle element
                sum_ += grid[i + 1][j + 1]
                max_sum = max(sum_, max_sum)
        return max_sum