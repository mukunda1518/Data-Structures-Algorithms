# Leetcode: https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return n
        res = 0
        l = 0
        count = 0
        for r in range(n):
            if nums[r] == 0: count += 1

            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1

            res = max(res, r - l + 1)
        return res