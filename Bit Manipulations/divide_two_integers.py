# Problem: https://leetcode.com/problems/divide-two-integers/

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.


# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        
        sign = + 1
        if dividend < 0 and divisor >= 0:
            sign = -1
        if dividend >= 0 and divisor < 0:
            sign = -1
        ans = 0
        n = abs(dividend)
        d = abs(divisor)
        while n >= d:
            count = 0
            while n >= d << (count + 1):
                count += 1
            ans += 1 << count
            n = n - d * (1 << count)
        if ans >= 2 ** 31 - 1 and sign == 1:
            return 2 ** 31 - 1
        if ans >= 2 ** 31 and sign == -1:
            return sign * 2 ** 31
        return sign * ans

