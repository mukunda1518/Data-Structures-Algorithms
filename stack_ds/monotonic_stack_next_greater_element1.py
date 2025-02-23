# Leetcode: https://leetcode.com/problems/next-greater-element-ii/
# Youtube: https://www.youtube.com/watch?v=7PrncD7v9YQ

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nge = [0] * n
        stack = []
        for i in range(2 * (n-1), -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            if i < n:
                nge[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        return nge
