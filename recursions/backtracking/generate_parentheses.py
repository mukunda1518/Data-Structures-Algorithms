# Leetcode: https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parentheses = "("
        res = []

        def backtrack(parentheses, open_p = 1, closed_p = 0):
            if open_p == closed_p == n:
                res.append(parentheses)
                return
            if open_p < n:
                backtrack(parentheses + "(", open_p + 1, closed_p)
            if closed_p < open_p:
                backtrack(parentheses + ")", open_p, closed_p + 1)

        backtrack(parentheses, 1, 0)
        return res