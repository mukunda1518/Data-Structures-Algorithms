# Problem - https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1

# You are given a number n. Find the total count of set bits for all numbers from 1 to n (both inclusive).

# Input: n = 4
# Output: 5
# Explanation: For numbers from 1 to 4. For 1: 0 0 1 = 1 set bits For 2: 0 1 0 = 1 set bits For 3: 0 1 1 = 2 set bits For 4: 1 0 0 = 1 set bits Therefore, the total set bits is 5.


class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        set_bit_count = 0
        for i in range(1, n + 1):
            while i > 0:
                i = i & (i - 1)
                set_bit_count += 1
        return set_bit_count
