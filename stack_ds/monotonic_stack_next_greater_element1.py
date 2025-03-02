# Leetcode: https://leetcode.com/problems/next-greater-element-ii/
# Youtube: https://www.youtube.com/watch?v=7PrncD7v9YQ

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nge = [0] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            if i < n:
                nge[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        return nge
