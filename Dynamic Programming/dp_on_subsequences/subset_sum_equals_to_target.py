# https://takeuforward.org/plus/dsa/problems/subset-sum-equals-to-target

# https://www.youtube.com/watch?v=fWX9xDmIzRI


class Solution:

    # Time Complexity - O(2^n)
    # Space Complexity - O(n)
    def is_subset_sum_recurr(self, i, arr, target):
        if target == 0:
            return True
        if i == 0:
            return arr[i] == target

        not_take = self.is_subset_sum_recurr(i - 1, arr, target)
        take = False
        if target >= arr[i]:
            take = self.is_subset_sum_recurr(i - 1, arr, target - arr[i])

        return not_take or take 

    # Time Complexity - O(n * target)
    # Space Complexity - O(n * target) + O(n)
    def is_subset_sum_memo(self, i, arr, target, dp):
        if target == 0:
            return True
        if i == 0:
            return arr[i] == target
        if dp[i][target] != -1:
            return dp[i][target]

        not_take = self.is_subset_sum_recurr(i - 1, arr, target, dp)
        take = False
        if target >= arr[i]:
            take = self.is_subset_sum_recurr(i - 1, arr, target - arr[i], dp)

        dp[i][target]= not_take or take 
        return dp[i][target]
    
    # Time Complexity - O(n * target)
    # Space Complexity - O(n * target)
    def is_subset_sum_tabulation(self, arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n)]

        # 1st base case
        for i in range(n):
            dp[i][0] = 1
        # 2nd base case
        if arr[0] <= target:
            dp[0][arr[0]] = 1

        # All 2 states
        for i in range(1, n):
            for k in range(1, target + 1):
                not_take = dp[i-1][k]
                take = 0
                if arr[i] <= k:
                    take = dp[i-1][k-arr[i]]
                dp[i][k] = not_take or take

        return dp[n-1][target]

    # Time Complexity - O(n * target)
    # Space Complexity - O(target)
    def is_subset_sum_tabu_space(self,arr, target):
        n = len(arr)
        prev = [0] * (target + 1)
        curr = [0] * (target + 1)

        # 1st base case
        prev[0] = 1
        curr[0] = 1
        # 2nd base case
        if arr[0] <= target:
            prev[arr[0]] = 1

        # All 2 states
        for i in range(1, n):
            for k in range(1, target + 1):
                not_take = prev[k]
                take = 0
                if arr[i] <= k:
                    take = prev[k-arr[i]]
                curr[k] = not_take or take
            prev = curr
        return prev[target]

    def isSubsetSum(self, arr, target):
        return self.is_subset_sum_tabu_space(arr, target)


     