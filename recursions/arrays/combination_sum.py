# Leetcode: https://leetcode.com/problems/combination-sum/description/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.


class Solution:

    def findCombinations(self, idx, n, target, arr, candidates, res):
        if target == 0:
            res.append(arr.copy())
            return
        elif n == idx:
            return
        
        if candidates[idx] <= target:
            arr.append(candidates[idx])
            self.findCombinations(idx, n, target - candidates[idx], arr, candidates, res)
            arr.pop()
        self.findCombinations(idx + 1, n, target, arr, candidates, res)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        res = []
        self.findCombinations(0, n, target, [], candidates, res)
        return res




        