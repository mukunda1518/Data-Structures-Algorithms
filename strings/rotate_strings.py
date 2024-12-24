# Leetcode: https://leetcode.com/problems/rotate-string/description/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)

        if n != m:
            return False

        return goal in s + s
