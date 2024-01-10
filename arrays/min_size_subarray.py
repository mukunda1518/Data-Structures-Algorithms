# Leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/description/



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, sum_ = 0, 0, 0
        len_ = len(nums)
        res = float("+inf")
        while l < len_ and r < len_:
            sum_ += nums[r]
            if sum_ >= target:
                res = min(res, r - l + 1)
                sum_ = sum_ - nums[l] - nums[r]
                l += 1
            else:
                r += 1
        return 0 if res == float("+inf") else res

    