# Youtube - https://www.youtube.com/watch?v=nttpF8kwgd4


# Problem: https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1


# Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 

# 1. Get ith bit

# 2. Set ith bit

# 3. Clear ith bit

# Note : For better understanding, we are starting bits from 1 instead 0. (1-based). You have to print space three space separated values ( as shown in output without a line break) and do not have to return anything.


# Example

# Input: 70 3
# Output: 1 70 66
# Explanation: Bit at the 3rd position from LSB is 1. (1 0 0 0 1 1 0) .The value of the given number after setting the 3rd bit is 70. The value of the given number after clearing 3rd bit is 66. (1 0 0 0 0 1 0)


class Solution:
    def bitManipulation(self, num, i):
        # get the ith bit
        ith_bit = (num >> (i - 1)) & 1
        # After setting ith bit
        set_ith_bit_num = (1 << (i - 1)) | num
        # after clearing ith bit
        clear_ith_bit_num = num & ~(1 << (i - 1))
        
        print(f"{ith_bit} {set_ith_bit_num} {clear_ith_bit_num}")
