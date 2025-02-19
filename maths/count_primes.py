
# Problem - https://leetcode.com/problems/count-primes/description/
# Youtube - https://www.youtube.com/watch?v=g5Fuxn_AvSk

# Given an integer n, return the number of prime numbers that are strictly less than n.

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Time Complexity - O(n) + O(n log(logn)) + O(n)

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1] * n 
        i = 2
        while i * i < n:
            if primes[i] == 1:
                j = i * i
                while j < n:
                    primes[j] = 0
                    j += i
            i += 1
        
        count = 0

        for i in range(2, n):
            count += 1 if primes[i] == 1 else 0
        return count

