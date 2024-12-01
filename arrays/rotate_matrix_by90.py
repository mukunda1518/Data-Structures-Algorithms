# Leetcode: https://leetcode.com/problems/rotate-image/description/


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose
        for i in range(n - 1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
        