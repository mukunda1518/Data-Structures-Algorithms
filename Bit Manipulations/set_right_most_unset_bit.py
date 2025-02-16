# Problem : https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1

# Given a non-negative number n . The problem is to set the rightmost unset bit in the binary representation of n.


# Input: n = 6
# Output: 7
# Explanation: The binary representation of 6 is 110. After setting right most bit it becomes 111 which is 7.



class Solution:
	def setBit(self, n):
		# code here
		return n | (n + 1)