# Problem: https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Input: nums = [4,1,2,1,2]

# Output: 4




class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans