# Leetcode: https://leetcode.com/problems/find-a-peak-element-ii/

# Time Complexity = O(n * log m)


class Solution:

    def get_max_element_index(self, mat, n, m, col):
        index = -1
        max_element = -1
        for i in range(n):
            if mat[i][col] > max_element:
                max_element = mat[i][col]
                index = i
        return index

    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        n = len(mat)
        m = len(mat[0])
        low, high = 0, m - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = self.get_max_element_index(mat, n, m, mid)
            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1

            