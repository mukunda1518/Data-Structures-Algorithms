# Leetcode: https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longest_len_of_plaindromes(self, s: str, n: int, l: int, r: int):
        max_len = 0
        string = ""
        while l >= 0 and r < n and s[l] == s[r]:
            if max_len < r - l + 1:
                max_len = r - l + 1
                string = s[l:r+1] 
            l -= 1
            r += 1
        return max_len, string

    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        pan_str = ""
        n = len(s)

        for i in range(n):
            # for odd length palindromes
            l = r = i
            len_, string = self.longest_len_of_plaindromes(s, n, l, r)
            if max_len < len_:
                max_len = len_
                pan_str = string
            # for even length palindromes
            l, r = i, i + 1
            len_, string = self.longest_len_of_plaindromes(s, n, l, r)
            if max_len < len_:
                max_len = len_
                pan_str = string
        return pan_str
    