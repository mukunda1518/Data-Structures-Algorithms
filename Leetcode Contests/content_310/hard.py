# Leetcode Question : https://leetcode.com/contest/weekly-contest-310/problems/longest-increasing-subsequence-ii/

# Note: Not optimised solution beacuse segment trees concepts need to learn

# Time Complexity : O(n^2)

class Solution:
    def lengthOfLIS(self, nums, k: int) -> int:
        n = len(nums)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            max_ = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i] and nums[j] - nums[i] <= k:
                    max_ = max(max_, res[j])
            res[i] = max_ + 1
        return max(res)
