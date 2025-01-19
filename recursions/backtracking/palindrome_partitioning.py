# Problem: https://leetcode.com/problems/palindrome-partitioning/description/


class Solution:

    def is_palindrome(self, start, end, s):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def solve(self, idx, n, s, partition, res):
        if idx == n:
            res.append(partition.copy())
            return

        for i in range(idx, n):
            if self.is_palindrome(idx, i, s):
                partition.append(s[idx:i+1])
                self.solve(i + 1, n, s, partition, res)
                partition.pop()

    def partition(self, s: str) -> list[list[str]]:
        res = []
        partition = []
        self.solve(0, len(s), s, partition, res)
        return res
