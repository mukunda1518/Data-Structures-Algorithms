# Leetcode: https://leetcode.com/problems/combination-sum-ii/description/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]


# Time Complexity is: 2^n * n + nlogn

class Solution:
    def findCombinations(self, idx, n, target, arr, candidates, res):
        if target == 0:
            res.append(arr.copy())
            return
        if idx == n:
            return

        for i in range(idx, n):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            arr.append(candidates[i])
            self.findCombinations(i + 1, n, target - candidates[i], arr, candidates, res)
            arr.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        self.findCombinations(0, n, target, [], candidates, res)
        return res
    
