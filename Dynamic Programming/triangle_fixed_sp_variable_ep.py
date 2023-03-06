# Problem Link: https://bit.ly/3K1cvqv
# Youtube Link: https://www.youtube.com/watch?v=SrP-PiLSYC0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=12
import copy


# Recursion
# Time Complexity - O( 2^(n * (n + 1) // 2) )
# Space Complexity - O(n)

def get_min_path_recur(r, c, arr, n):
    if r == n - 1:
        return arr[r][c]
    down = arr[r][c] + get_min_path_recur(r + 1, c, arr, n)
    diagonal = arr[r][c] + get_min_path_recur(r + 1, c + 1, arr, n)
    return min(down, diagonal)


# Memoization Method : Top - Down Approach
# Time Complexity - O(n * n)
# Space Complexity - O(n) + O(n * n)

def get_min_path_memo(r, c, dp, arr, n):
    if r == n - 1:
        return arr[r][c]
    if dp[r][c] != -1:
        return dp[r][c]
    down = arr[r][c] + get_min_path_memo(r + 1, c, dp, arr, n)
    diagonal = arr[r][c] + get_min_path_memo(r + 1, c + 1, dp, arr, n)
    dp[r][c] = min(down, diagonal)
    return dp[r][c]


# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n * n)
# Space Complexity - O(n * n)


def get_min_paths_tabulation(arr, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[n-1] = copy.deepcopy(arr[n-1])

    for i in range(n-2, -1, -1):
        for j in range(i, -1, -1):
            down = arr[i][j] + dp[i+1][j]
            diagonal = arr[i][j] + dp[i+1][j+1]
            dp[i][j] = min(down, diagonal)
    return dp[0][0]

# Tabulation method - Optimised space
# Time Complexity - O(n * n)
# Space Complexity - O(n) + O(n * n)


def get_min_paths_space_optimised(arr, n):
    last = copy.deepcopy(arr[n-1])
    for i in range(n-2, -1, -1):
        curr = [0] * n
        for j in range(i, -1, -1):
            down = arr[i][j] + last[j]
            diagonal = arr[i][j] + last[j+1]
            curr[j] = min(down, diagonal)
        last = curr
    return last[0]


# main function


if __name__ == "__main__":
    n = 4
    arr = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]

    # Recursion
    print(get_min_path_recur(0, 0, arr, n))

    # Memoization
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    print(get_min_path_memo(0, 0, dp, arr, n))

    # Tabulation
    print(get_min_paths_tabulation(arr, n))

    # Space Optimized
    print(get_min_paths_space_optimised(arr, n))

