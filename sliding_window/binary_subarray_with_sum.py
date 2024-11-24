# Leetcode: https://leetcode.com/problems/binary-subarrays-with-sum/



class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def helper(x):
            if x < 0: return 0
            res = 0
            l = 0
            curr_sum = 0
            for r in range(len(nums)):
                curr_sum += nums[r]
                while curr_sum > x:
                    curr_sum -= nums[l]
                    l += 1
                res += r - l + 1
            return res
    
        return helper(goal) - helper(goal - 1) 