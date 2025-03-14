
# Leetcode: https://leetcode.com/problems/assign-cookies/
# https://www.youtube.com/watch?v=DIX2p7vb9co


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        l, r = 0, 0
        while l < n and r < m:
            if s[r] >= g[l]:
                r += 1
                l += 1
            else:
                r += 1
        return l
        