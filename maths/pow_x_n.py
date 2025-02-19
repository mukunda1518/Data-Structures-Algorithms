
# Leetcode: https://leetcode.com/problems/powx-n/description/
# Youtube: https://www.youtube.com/watch?v=hFWckDXE-K8

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        m = n
        n = abs(n)
        while n > 0:
            if n & 1 == 1:
                ans = ans * x
                n = n - 1
            else:
                n = n // 2
                x = x * x
        if m < 0:
            ans = 1.0 / ans
        return ans
