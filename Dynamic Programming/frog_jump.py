    # Problem : https://www.codingninjas.com/codestudio/problems/frog-jump_3621012
# Solution: https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=4

# Recursion
# Time Complexity - O(2^n)
# Space Complexity - O(1) without stack space
def get_minimum_energy(n, heights):
    if n == 0:
        return 0
    left = get_minimum_energy(n - 1, heights) + abs(heights[n] - heights[n-1])
    right = float("+inf")
    if n > 1:
        right = get_minimum_energy(n - 2, heights) + abs(heights[n] - heights[n-2])
    return min(left, right)


# Memoization Method : Top - Down Approach
# Time Complexity - O(n)
# Space Complexity - O(n)

def get_minimum_energy_memo(n, heights, dp):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    left = get_minimum_energy_memo(n - 1, heights, dp) + abs(heights[n] - heights[n-1])
    right = float("+inf")
    if n > 1:
        right = get_minimum_energy_memo(n - 2, heights, dp) + abs(heights[n] - heights[n-2])
    dp[n] = min(left, right)
    return dp[n]

# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n)
# Space Complexity - O(n)


def get_minimum_energy_table(n, heights):
    dp = [0]
    for i in range(1, n):
        one_step = dp[i - 1] + abs(heights[i] - heights[i-1])
        two_steps = float("+inf")
        if i > 1:
            two_steps = dp[i - 2] + abs(heights[i] - heights[i-2])
        mini = min(one_step, two_steps)
        dp.append(mini)
    return dp[-1]

# Tabulation method - Optimised space
# Time Complexity - O(n)
# Space Complexity - O(1)


def get_minimum_energy_space_optimised(n, heights):
    prev = 0
    prev2 = 0
    for i in range(1, n):
        one_step = prev + abs(heights[i] - heights[i-1])
        two_steps = float("+inf")
        if i > 1:
            two_steps = prev2 + abs(heights[i] - heights[i-2])
        prev2 = prev
        prev = min(one_step, two_steps)
    return prev


if __name__ == "__main__":
    n = 6
    heights = [30, 10, 60, 10, 60, 50]
    print(get_minimum_energy(n-1, heights))

    dp = [-1] * n
    print(get_minimum_energy_memo(n-1, heights, dp))

    print(get_minimum_energy_table(n, heights))

    print(get_minimum_energy_space_optimised(n, heights))


    
