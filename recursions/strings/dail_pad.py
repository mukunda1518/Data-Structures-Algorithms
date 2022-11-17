# Leetcode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List

arr1 = []

def dail_pad(p, up):
    if up == "":
        print(p)
        return
    digit = int(up[0])
    s = (digit - 1) * 3
    e = (digit) * 3
    for i in range(s, e):
        char = chr(i + 97)
        dail_pad(p + char, up[1:])

def dail_pad_list(p, up):
    if up == "":
        arr1.append(p)
        return[p]
    digit = int(up[0])
    s = (digit - 1) * 3
    e = (digit) * 3
    arr = []
    for i in range(s, e):
        char = chr(i + 97)
        arr.extend(dail_pad_list(p + char, up[1:]))
    return arr
    
if __name__ == "__main__":
    dail_pad("", "12")
    print(dail_pad_list("", "12"))
    print(arr1)

# Time Complexity = O(4 ^ n)
# Space Complexity = O(4 ^ n)

dict1 = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


class Solution:
    def get_letter_combinations(self, p_str, up_str):
        if up_str == "":
            return [p_str]
        arr = []
        char = up_str[0]
        for i in dict1[char]:
            arr.extend(self.get_letter_combinations(p_str + i, up_str[1:]))
        return arr

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # return self.get_letter_combinations("", digits)

        # Iterative Approach
        results = [""]
        for digit in digits:
            new_results = []
            for char in dict1[digit]:
                for result in results:
                    new_results.append(result + char)
            results = new_results
        return new_results


