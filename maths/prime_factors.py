# Problem: https://www.geeksforgeeks.org/problems/prime-factors5052/1

# Given a number N. Find its unique prime factors in increasing order.

# Input: N = 100
# Output: 2 5
# Explanation: 2 and 5 are the unique prime
# factors of 100.


# Time Complexity - O(sqrt(n) * log(n))


class Solution:
    def AllPrimeFactors(self, N):
        prime_factors = []
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                prime_factors.append(i)
            while N % i == 0:
                N = N // i
        if N > 1:
            prime_factors.append(N)
        return prime_factors
