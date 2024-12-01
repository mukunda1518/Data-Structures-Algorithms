# Leetcode: https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # For col - matrix[0][..]
        # For row - matrix[..][0]
        col1 = 1
        for i in range(m):
            for j in range(n): 
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col1 = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        # for first row
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0

        # for first column
        if col1 == 0:
            for j in range(m):
                matrix[j][0] = 0