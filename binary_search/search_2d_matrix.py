# Leetcode: https://leetcode.com/problems/search-a-2d-matrix/description/


class Solution:
    def is_target_found(self, arr, n, target):
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for arr in matrix:
            if target >= arr[0] and target <= arr[-1]:
                return self.is_target_found(arr, n, target)
        return False


# Time Complexity - O(log n * m)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low, high = 0, n * m - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = mid // n
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
