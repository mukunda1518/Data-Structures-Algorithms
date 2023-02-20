# Problem Link: https://bit.ly/34uoYCG
# Youtube Link: https://www.youtube.com/watch?v=sdE0A2Oxofw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=9


# Recursion
# Time Complexity - O( 2^(m * n) )
# Space Complexity - O(m - 1) + O(n - 1)

def get_unique_paths_recur(r, c):
    if r == 0 and c == 0:
        return 1
    if r < 0 or c < 0:
        return 0
    left = get_unique_paths_recur(r, c - 1)
    right = get_unique_paths_recur(r - 1, c)
    return left + right


# Memoization Method : Top - Down Approach
# Time Complexity - O(m * n)
# Space Complexity - O(m - 1) + O(n - 1) + O(m * n)

def get_unique_paths_memo(r, c, dp):
    if r == 0 and c == 0:
        return 1
    if r < 0 or c < 0:
        return 0
    if dp[r][c] != -1:
        return dp[r][c]
    left = get_unique_paths_memo(r, c - 1, dp)
    right = get_unique_paths_memo(r - 1, c, dp)
    dp[r][c] = left + right
    return dp[r][c]


# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n * m)
# Space Complexity - O(n * m)


def get_unique_paths_tabulation(r, c):
    dp = [[-1 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            up, left = 0, 0
            if i > 0:
                left = dp[i - 1][j]
            if j > 0:
                up = dp[i][j - 1]
            dp[i][j] = up + left
    return dp[r - 1][c - 1]


# Tabulation method - Optimised space
# Time Complexity - O(n * m)
# Space Complexity - O(n)


def get_unique_paths_space_optimised(r, c):
    dp = [0] * c

    for i in range(r):
        temp = [0] * c
        for j in range(c):
            if i == 0 and j == 0:
                temp[j] = 1
                continue
            temp[j] = dp[j] + temp[j - 1]
        dp = temp
    return dp[c-1]


# main function


if __name__ == "__main__":
    m = int(input())
    n = int(input())

    # Recursion
    print(get_unique_paths_recur(m - 1, n - 1))

    # Memoization
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    print(get_unique_paths_memo(m - 1, n - 1, dp))

    # Tabulation
    print(get_unique_paths_tabulation(m, n))

    # Space Optimized
    print(get_unique_paths_space_optimised(m, n))

