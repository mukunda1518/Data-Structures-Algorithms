# Leetcode: https://leetcode.com/problems/valid-anagram/

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = defaultdict(int)

        for char in s:
            counter[char] += 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
    
        return True
    
    
    
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        xor_sum = 0
        frequency = [0] * 26
        
        for i in range(len(s)):
            xor_sum ^= ord(s[i]) ^ ord(t[i]) # XOR both characters
            frequency[ord(s[i]) - ord('a')] += 1 # Increment for s
            frequency[ord(t[i]) - ord('a')] -= 1 # Decrement for t
        
        if xor_sum != 0: # If XOR isn't zero, they're not anagrams
            return False
        
        if any(freq != 0 for freq in frequency): # Check frequency counts
            return False
        
        return True