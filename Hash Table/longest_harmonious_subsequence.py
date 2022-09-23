#Leetcode: https://leetcode.com/problems/longest-harmonious-subsequence/

from collections import defaultdict
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_freq = defaultdict(int)
        for num in nums:
            nums_freq[num] += 1
        long_len = 0
        for key in nums_freq.keys():
            if key + 1 in nums_freq:
                len_ = nums_freq[key] + nums_freq[key+1]
                long_len = max(long_len, len_)
        return long_len