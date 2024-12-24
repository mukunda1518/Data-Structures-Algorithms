

# Leetcode: https://leetcode.com/problems/string-to-integer-atoi/




class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        res = 0
        sign = 1

        symbols = {
            "-": -1,
            "+": 1
        }

        i = 0
        # step1 for white spaces
        while i < n and s[i] == " ":
            i += 1

        # step2
        if i < n and s[i] in symbols:
            sign = symbols[s[i]]
            i += 1

        # step3
        while i < n and s[i].isdigit():
            res = (res * 10) + int(s[i])
            i += 1
    
        # bound check
        val = res * sign
        
        if val <= -2**31 - 1:
            return -2**31
        elif val >= 2**31 - 1:
            return 2**31 - 1

        return val
