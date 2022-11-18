# Problem: https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261
# Solution: https://www.youtube.com/watch?v=GrMBfJNk_NY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=6

# Recursion
# Time Complexity - O(2^n)
# Space Complexity - O(1) without stack space
# Space Complexity - O(2^n) with stack space

def max_sum(n, nums):
    if n == 0:
        return nums[0]
    if n < 0:
        return 0

    pick_val = nums[n] + max_sum(n - 2, nums)
    non_pick_val = 0 + max_sum(n - 1, nums)

    return max(pick_val, non_pick_val)


# Memoization Method : Top - Down Approach
# Time Complexity - O(n)
# Space Complexity - O(n) + O(n) (stack space)


def max_sum_memo(n, nums, dp):
    if n == 0:
        return nums[0]
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]

    pick_val = nums[n] + max_sum(n - 2, nums)
    non_pick_val = 0 + max_sum(n - 1, nums)

    dp[n] = max(pick_val, non_pick_val)
    return dp[n]


# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n)
# Space Complexity - O(n)

def max_sum_table(n, nums):
    dp = [nums[0]]
    for i in range(1, n):
        take = nums[i]
        take += dp[i - 2] if i > 1 else 0
        not_take = 0 + dp[i - 1]
        dp.append(max(take, not_take))
    return dp[-1]


# Tabulation method - Optimised space
# Time Complexity - O(n)
# Space Complexity - O(1)


def max_sum_space_optimized(n, nums):
    prev = nums[0]
    prev1 = 0

    for i in range(1, n):
        take = nums[i] + prev1
        non_take = 0 + prev
        prev1 = prev
        prev = max(take, non_take)
    return prev


if __name__ == "__main__":
    n = 9
    nums = [1, 2, 3, 1, 3, 5, 8, 1, 9]
    print(max_sum(n-1, nums))

    dp = [-1] * n
    print(max_sum_memo(n-1, nums, dp))

    print(max_sum_table(n, nums))

    print(max_sum_space_optimized(n, nums))
