
# Problem: https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

# Input: arr[] = [2, 5, 1, 4, 3], target = 10
# Output: 3
# Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.



#User function Template for python3

class Solution:
    
    def get_perfect_sum_count(self, idx, arr, target, curr_s, n):
        
        if idx >= n:
            return 1 if target == curr_s else 0
        
        count = 0

        for i in range(idx, n):
            count += self.get_perfect_sum_count(i + 1, arr, target, curr_s + arr[i], n)
        
        if curr_s == target:
            count += 1

        return count 

    def perfectSum(self, arr, target):
        return self.get_perfect_sum_count(0, arr, target, 0, len(arr))
