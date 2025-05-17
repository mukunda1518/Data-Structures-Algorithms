# https://takeuforward.org/plus/dsa/problems/count-subsets-with-sum-k

# https://www.youtube.com/watch?v=ZHyb-A2Mte4


# Count subsets with sum K
# Given an array arr of n integers and an integer K, count the number of subsets of the given array that have a sum equal to K. Return the result modulo 109+7.

# Input: arr = [2, 3, 5, 16, 8, 10], K = 10
# Output: 3
# Explanation: The subsets are [2, 8], [10], and [2, 3, 5].


class Solution:

    # TC - O(2^n)
    # SC - O(n)
    def count_sum_k_recurr(self, idx, arr, k):
        if k == 0:
            return 1
        if idx == 0: 
            return 1 if arr[idx] == k else 0

        not_take = self.count_sum_k_recurr(idx - 1, arr, k)
        take = 0
        if arr[idx] <= k:
            take = self.count_sum_k_recurr(idx-1, arr, k - arr[idx])
        return take + not_take

    # TC - O(n * k)
    # SC - O(n * k) + O(n)
    def count_sum_k_recurr(self, idx, arr, k, dp):
        if k == 0:
            return 1
        if idx == 0: 
            return 1 if arr[idx] == k else 0
        if dp[idx][k] != -1:
            return dp[idx][k]

        not_take = self.count_sum_k_recurr(idx - 1, arr, k)
        take = 0
        if arr[idx] <= k:
            take = self.count_sum_k_recurr(idx-1, arr, k - arr[idx])
        dp[idx][k] = take + not_take
        return dp[idx][k]
    
    # TC - O(n * k)
    # SC - O(n * k)
    def count_sum_k_tabu(self, arr, k):
        n = len(arr)
        dp = [[0] * (k+1) for _ in range(n)]
        # 1st base case
        for i in range(n):
            dp[i][0] = 1
        # 2nd base case
        if arr[0] <= k:
            dp[0][arr[0]] += 1
        
        # steps
        for i in range(1, n):
            for s in range(0, k + 1):
                not_take = dp[i-1][s]
                take = 0
                if arr[i] <= s:
                    take = dp[i-1][s-arr[i]]
                dp[i][s] = not_take + take
        return dp[n-1][k]
    
    # TC - O(n * k)
    # SC - O(k)
    def count_sum_k_space(self, arr, k):
        n = len(arr)
        prev = [0] * (k + 1)
        curr = [0] * (k + 1)
        # 1st base case
        prev[0] = 1
        curr[0] = 1
        # 2nd base case
        if arr[0] <= k:
            prev[arr[0]] += 1
        
        # steps
        for i in range(1, n):
            for s in range(0, k + 1):
                not_take = prev[s]
                take = 0
                if arr[i] <= s:
                    take = prev[s-arr[i]]
                curr[s] = not_take + take
            curr = prev
        return prev[k]

    def perfectSum(self, arr, K):
        return self.count_sum_k_space(arr, K)
        return self.count_sum_k_tabu(arr, K)
     
