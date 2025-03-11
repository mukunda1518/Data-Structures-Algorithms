# Leetcode: https://leetcode.com/problems/remove-k-digits/
# https://www.youtube.com/watch?v=jmbuRzYPGrg


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining k digits from the end of the stack
        stack = stack[:-k] if k > 0 else stack

        # Remove leading zeros
        res = "".join(stack).lstrip("0")

        return res if res else "0"

