# Leetcode: https://leetcode.com/problems/number-of-common-factors/description/


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        min_num = min(a, b)
        for i in range(1, min_num + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count