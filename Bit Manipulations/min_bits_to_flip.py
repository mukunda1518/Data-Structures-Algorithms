# Problem : https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.



class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_num = start ^ goal
        ans = 0

        while xor_num > 0:
            ans += xor_num & 1
            xor_num = xor_num >> 1

        return ans
