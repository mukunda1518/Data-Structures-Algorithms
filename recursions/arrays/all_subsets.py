# Leetcode: https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, return all possible subsets

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


class Solution:

    def get_all_subsets(self, idx, arr, nums, res, n):
        res.append(arr.copy())
        if idx >= n:
            return
        for i in range(idx, n):
            arr.append(nums[i])
            self.get_all_subsets(i + 1, arr, nums, res, n)
            arr.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.get_all_subsets(0, [], nums, res, len(nums))
        return res
