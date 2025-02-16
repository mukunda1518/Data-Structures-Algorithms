# Problem: https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1

# You are given two numbers a and b. Your task is to swap the given two numbers.

# Note: Try to do it without a temporary variable.

# Input: a = 13, b = 9
# Output: 9 13
# Explanation: After swapping it becomes 9 and 13.


class Solution:
    def get(self, a, b):
        #code here
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b
