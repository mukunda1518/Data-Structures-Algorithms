# Leetcode: https://leetcode.com/problems/spiral-matrix/description/


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        left, right = 0, m - 1
        top, bottom = 0, n - 1
        res = []
        while top <= bottom and left <= right:
            # Left -> Right
            for i in range(left, right + 1, 1):
                res.append(matrix[top][i])
            top += 1
            # Top -> Bottom
            for i in range(top, bottom + 1, 1):
                res.append(matrix[i][right])
            right -= 1
            # Right -> Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
            bottom -= 1
            # Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
            left += 1
    
        return res
            