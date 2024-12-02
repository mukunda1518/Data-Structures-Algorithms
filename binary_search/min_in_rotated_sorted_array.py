# Leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        res = float("+inf")
        while low <= high:
            mid = low + (high - low) // 2
            if nums[low] <= nums[high]:
                res = min(res, nums[low])
                break

            if nums[low] <= nums[mid]:
                res = min(res, nums[low])
                low = mid + 1
            else:
                res = min(res, nums[mid])
                high = mid - 1
        return res
    