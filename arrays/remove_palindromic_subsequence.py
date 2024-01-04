# Leetcode: https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if not s:
        #     return 0
        # elif s == s[::-1]:
        #     return 1
        # else:
        #     return 2

        if not s:
            return 0
        count = 1
        len_ = len(s)
        for i in range(len_):
            if s[i] != s[len_ - i - 1]:
                count += 1
                break
        return count

