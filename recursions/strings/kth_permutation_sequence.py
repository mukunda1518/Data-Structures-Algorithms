# Leetcode: https://leetcode.com/problems/permutation-sequence/

# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.



class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = []
        fact = 1
        for i in range(1, n):
            fact *= i
            numbers.append(i)
        numbers.append(n)

        k = k -1
        ans = ""

        while True:
            pos = k // fact
            ans = ans + str(numbers[pos])
            numbers.pop(pos)
            len_ = len(numbers)

            if len_ == 0:
                break

            k = k % fact
            fact = fact // len_

        return ans
