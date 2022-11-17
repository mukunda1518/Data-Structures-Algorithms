# Leetcode: https://leetcode.com/problems/climbing-stairs/

# find no of ways climbing the n steps, if we can take 1 step at a time or 2 steps at a time

# Recursion
# Time Complexity - O(2^n)
# Space Complexity - O(1) without auxiliary space
def no_of_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return no_of_ways(n - 1) + no_of_ways(n - 2)

# Memoization Method : Top - Down Approach
# Time Complexity - O(n)
# Space Complexity - O(n)


def no_of_ways_memo(n, dp):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = no_of_ways_memo(n - 1, dp) + no_of_ways_memo(n - 2, dp)
    return dp[n]

# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n)
# Space Complexity - O(n)


def no_of_ways_table(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        count = dp[-1] + dp[-2]
        dp.append(count)
    return dp[-1]

# Tabulation method - Optimised space
# Time Complexity - O(n)
# Space Complexity - O(1)


def no_of_ways_space_optimised(n):
    prev = 1
    prev2 = 1
    for i in range(2, n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev


if __name__ == "__main__":
    n = int(input())
    print(no_of_ways(n))

    dp = [-1] * (n + 1)
    print(no_of_ways_memo(n, dp))

    print(no_of_ways_table(n))

    print(no_of_ways_space_optimised(n))
