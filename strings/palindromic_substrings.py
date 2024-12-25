# Leetcode: https://leetcode.com/problems/palindromic-substrings/


class Solution:

    def countplaindromes(self, s: str, n: int, l: int, r: int):
        res = 0
        while l >= 0 and r < n and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            # for odd length palindromes
            l = r = i
            res += self.countplaindromes(s, n, l, r)
            # for even length palindromes
            l, r = i, i + 1
            res += self.countplaindromes(s, n, l, r)
        return res
