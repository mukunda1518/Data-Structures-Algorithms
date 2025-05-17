# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/


# https://www.youtube.com/watch?v=GS_OqZb2CWc


### only positive elements



# Time Complexity - O(n * total_sum)
    # Space Complexity - O(n * total_sum)
class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        dp = [[0] * (total_sum + 1) for _ in range(n)]
        # 1st base case
        for i in range(n):
            dp[i][0] = 1
        # 2nd base case
        if nums[0] <= total_sum:
            dp[0][nums[0]] = 1
        
        # All 2 states
        for i in range(1, n):
            for k in range(1, total_sum + 1):
                not_take = dp[i-1][k]
                take = 0
                if nums[i] <= k:
                    take = dp[i-1][k-nums[i]]
                dp[i][k] = not_take or take
        
        mini = 1e9
        for s in range(0, total_sum // 2):
            if dp[n-1][s]:
                s1 = total_sum - s
                mini = min(mini, abs(s1-s))
        return mini

        