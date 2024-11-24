# Leetcode: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c_dict = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        l = 0
        n = len(s)
        for r in range(n):
            if s[r] in ['a', 'b', 'c']:
                c_dict[s[r]] += 1
            while c_dict['a'] and c_dict['b'] and c_dict['c']:
                res += n - r
                c_dict[s[l]] -= 1
                l += 1
        return res


        