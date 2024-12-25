# Leetcode: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/


from collections import defaultdict

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            mp = defaultdict(int)
            for j in range(i, n):
                mp[s[j]] += 1
                values = mp.values()
                mx = max(values)
                mn = min(values)
                res += mx - mn
        return res

        