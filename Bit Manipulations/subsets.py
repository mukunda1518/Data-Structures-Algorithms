# Problem:  https://leetcode.com/problems/subsets/

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Using bit manipulations
        n = len(nums)
        for num in range(2**n):
            sub_set = []
            for i in range(n):
                if num & (1 << i):
                    sub_set.append(nums[i])
            res.append(sub_set)
        return res
