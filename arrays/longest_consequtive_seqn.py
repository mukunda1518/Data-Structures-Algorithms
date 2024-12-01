# Leetcode: https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
    
        nums_s = set(nums)
        longest = 1
        curr_count = 0
        for num in nums:
            # num is not the starting element of the sequence
            if num - 1 in nums_s:
                continue

            curr_count = 0
            while num in nums_s:
                curr_count += 1
                num += 1
            longest = max(longest, curr_count)

        return longest
