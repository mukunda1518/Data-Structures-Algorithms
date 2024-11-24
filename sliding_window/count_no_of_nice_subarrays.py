# Leetcode: https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res = 0
        l, m = 0, 0
        odd_count = 0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd_count += 1

            while odd_count > k:
                if nums[l] % 2:
                    odd_count -= 1
                l += 1
                m = l

            if odd_count == k:
                while not nums[m] % 2:
                    m += 1
                res += m - l + 1
        return res
