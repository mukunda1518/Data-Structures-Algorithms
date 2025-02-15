# Leetcode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/



class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        digits_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        len_ = len(digits)

        def backtrack(i, curr_str):
            if len(curr_str) == len_:
                res.append(curr_str)
                return
            for c in digits_to_char[digits[i]]:
                backtrack(i + 1, curr_str + c)
        
        if digits:
            backtrack(0, "")
        return res
