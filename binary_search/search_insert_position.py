# Leetcode: https://leetcode.com/problems/search-insert-position/description/


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        res = n
        while low <= high:
            mid = low + (high-low) // 2
            if target <= nums[mid]:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

