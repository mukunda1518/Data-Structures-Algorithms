# Problem: https://www.geeksforgeeks.org/problems/prime-factorization-using-sieve/1

# You are given a positive number N. Using the concept of Sieve, compute its prime factorisation.

# Input: 
# N = 12246
# Output: 
# 2 3 13 157
# Explanation: 
# 2*3*13*157 = 12246 = N.



class Solution:
    def sieve(self):
        self.primes = [i for i in range(2 * 10**5 + 1)]
        i = 2
        while i * i <= (2 * 10**5):
            if self.primes[i] == i:
                j = i * i
                while j <= (2 * 10**5):
                    if self.primes[j] == j:
                        self.primes[j] = i
                    j += i
            i += 1

    def findPrimeFactors(self, N):
        # Code here
        prime_factors = []
        while N != 1:
            prime_factors.append(self.primes[N])
            N = N // self.primes[N]
        return prime_factors