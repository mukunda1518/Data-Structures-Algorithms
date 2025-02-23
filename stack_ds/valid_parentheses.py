# Leetcode: https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in map_.values():
                stack.append(char)
            else:
                if not stack or map_[char] != stack.pop():
                    return False

        return not stack