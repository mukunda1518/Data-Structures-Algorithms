# Leetcode: https://leetcode.com/problems/sum-of-subarray-minimums/


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = [] # (index, num)
        for i, num in enumerate(arr):
            while stack and num < stack[-1][1]:
                index, element = stack.pop()
                left = index - stack[-1][0] if stack else index + 1 
                right = i - index
                res = (res + left * right * element) % MOD
            stack.append((i, num))
        for i in range(len(stack)):
            index, element = stack[i]
            left = index - stack[i - 1][0] if i > 0 else index + 1
            right = stack[-1][0] - index + 1
            res = (res + left * right * element) % MOD
        return res

