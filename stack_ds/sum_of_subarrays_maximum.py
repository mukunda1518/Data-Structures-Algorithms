# https://www.youtube.com/watch?v=aX1F2-DrBkQ

# Refer minimum first

class Solution:
    def sumSubarrayMaxs(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = [] # (index, element)

        for i, num in enumerate(arr):
            while stack and stack[-1][1] < num:
                j, n = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + n * left * right) % MOD
            stack.append((i, num))
        
        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            res = (res + n * left * right) % MOD
        return res