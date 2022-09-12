# Leetcode Question: https://leetcode.com/contest/weekly-contest-310/problems/optimal-partition-of-string/
class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 0
        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                count += 1
                seen = set(char)
        return count + 1
