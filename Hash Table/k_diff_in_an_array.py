# Leetcode: https://leetcode.com/problems/k-diff-pairs-in-an-array/submissions/


from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_dict = Counter(nums)
        pairs = 0
        for key in nums_dict:
            if (k > 0 and k + key in nums_dict) or (k == 0 and nums_dict[key] > 1):
                pairs += 1 
        return pairs