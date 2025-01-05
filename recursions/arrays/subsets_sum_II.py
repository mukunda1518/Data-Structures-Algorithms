# Leetcode: https://leetcode.com/problems/subsets-ii/

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]




class Solution:

    def find_subsets(self, idx, n, arr, nums, res):
        res.append(arr.copy())
        if n == idx:
            return
        
        for i in range(idx, n):
            if i != idx and nums[i] == nums[i-1]: 
                continue
            arr.append(nums[i])
            self.find_subsets(i + 1, n, arr, nums, res)
            arr.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        self.find_subsets(0, len(nums), [], nums, res)
        return res
        