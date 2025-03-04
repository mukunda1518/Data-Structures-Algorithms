# Leetcode: https://leetcode.com/problems/sum-of-subarray-ranges/

# https://www.youtube.com/watch?v=aX1F2-DrBkQ


class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        smallest_res = 0
        largest_res = 0
        stack = [] # (index, element)

        for i, num in enumerate(nums):
            while stack and stack[-1][1] > num:
                j, n = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                smallest_res = (smallest_res + n * left * right)
            stack.append((i, num))
        
        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(nums) - j
            smallest_res = (smallest_res + n * left * right)
        
        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                j, n = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                largest_res = (largest_res + n * left * right)
            stack.append((i, num))
        
        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(nums) - j
            largest_res = (largest_res + n * left * right)

        return largest_res - smallest_res

