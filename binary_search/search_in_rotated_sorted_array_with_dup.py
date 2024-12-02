# Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        res = False

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                res = True
                break
            elif nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return res
