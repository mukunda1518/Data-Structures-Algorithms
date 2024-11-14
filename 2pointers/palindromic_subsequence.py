# Leetcode: https://leetcode.com/problems/remove-palindromic-subsequences/



class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2
    
class Solution1:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        lp, rp = 0, len(s) - 1
        while lp < rp:
            if s[lp] != s[rp]:
                return 2
            lp += 1
            rp -= 1
        return 1



if __name__ == "__main__":
    sequence = input()
    print(Solution().removePalindromeSub(sequence))