# Problem : https://www.codingninjas.com/codestudio/problems/frog-jump_3621012
# Solution: https://www.youtube.com/watch?v=Kmh3rhyEtB8&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=5

from collections import deque

# Recursion
# Time Complexity - O(k^n)
# Space Complexity - O(1) without stack space


def get_minimum_energy(n, heights, k):
    if n == 0:
        return 0
    min_val = float("+inf")
    for i in range(1, k+1):
        if n >= i:
            val = get_minimum_energy(n - i, heights, k) + abs(heights[n] - heights[n - i])
            min_val = min(min_val, val)
    return min_val

# Memoization Method : Top - Down Approach
# Time Complexity - O(n * k)
# Space Complexity - O(n)


def get_minimum_energy_memo(n, heights, k, dp):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]

    min_val = float("+inf")
    for i in range(1, k+1):
        if n >= i:
            val = get_minimum_energy_memo(n - i, heights, k, dp) + abs(heights[n] - heights[n - i])
            min_val = min(min_val, val)
    dp[n] = min_val
    return min_val


# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n * k)
# Space Complexity - O(n)


def get_minimum_energy_table(n, heights, k):
    dp = [0]

    for i in range(1, n):
        min_val = float("+inf")
        for j in range(1, k+1):
            if i >= j:
                val = dp[i - j] + abs(heights[i] - heights[i - j])
                min_val = min(min_val, val)
        dp.append(min_val)
    return dp[-1]


# Tabulation method - Optimised space
# Time Complexity - O(n)
# Space Complexity - O(k) - if k is n - O(n)


def get_minimum_energy_space_optimized(n, heights, k):
    dp = deque()
    dp.append(0)

    for i in range(1, n):
        min_val = float("+inf")
        for j in range(1, k+1):
            if i >= j:
                if i > k:
                    index = k - j
                else:
                    index = i - j
                val = dp[index] + abs(heights[i] - heights[i - j])
                min_val = min(min_val, val)
        if len(dp) == k:
            dp.popleft()
        dp.append(min_val)

    return dp[-1]


if __name__ == "__main__":
    n, k = 10, 4
    heights = [10, 20, 5, 30, 10, 20, 10, 40, 50, 10]
    print(get_minimum_energy(n - 1, heights, k))

    dp = [-1] * n
    print(get_minimum_energy_memo(n - 1, heights, k, dp))

    print(get_minimum_energy_table(n, heights, k))

    print(get_minimum_energy_space_optimized(n, heights, k))



