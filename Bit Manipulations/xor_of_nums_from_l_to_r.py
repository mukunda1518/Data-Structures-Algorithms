# youtube - https://www.youtube.com/watch?v=WqGb7159h7Q

# Problem - https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1

# You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].

# Input: 
# L = 4, R = 8 
# Output:
# 8 
# Explanation:
# 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8



class Solution:
    def xor_upto_n(self, n):
        ans = None
        if n % 4 == 0:
            ans = n
        if n % 4 == 1:
            ans = 1
        if n % 4 == 2:
            ans = n + 1
        if n % 4 == 3:
            ans = 0
        return ans
    
    def findXOR(self, l, r):
        xor_l = self.xor_upto_n(l - 1)
        xor_r = self.xor_upto_n(r)
        
        return xor_l ^ xor_r