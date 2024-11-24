# Leetcode: https://leetcode.com/problems/subarrays-with-k-different-integers/description/
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        res = 0
        l, m = -1, 0
        mp = defaultdict(int)
        for r in range(len(nums)):
            mp[nums[r]] += 1
            while len(mp) > k or mp[nums[m]] > 1:
                if len(mp) > k:
                    l = m
                if mp[nums[m]] > 1:
                    mp[nums[m]] -= 1
                else:
                    del mp[nums[m]]
                m += 1
            if len(mp) == k:
                res += m - l
        return res
