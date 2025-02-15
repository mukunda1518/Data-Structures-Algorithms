# Problem: https://www.geeksforgeeks.org/problems/odd-or-even3618/1
    
# Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.

# Input: n = 15
# Output: false
# Explanation: The number is not divisible by 2

#User function Template for python3
class Solution:
    def isEven (self, n):
        # code here 
        
        return  n & 1 == 0