# Problem Link : https://takeuforward.org/data-structure/dynamic-programming-ninjas-training-dp-7/

# Youtube video : https://www.youtube.com/watch?v=AE39gJYuRog&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=8


# Recursion
# Time Complexity - O(2^n)
# Space Complexity - O(n) + O(n * 4) * 3
def max_points_recur(arr, day, last):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, arr[day][task])
        return maxi
    maxi = 0
    for task in range(3):
        if task != last:
            val = arr[day][task] + max_points_recur(arr, day - 1, task)
            maxi = max(maxi, val)
    return maxi

# Memoization Method : Top - Down Approach
# Time Complexity - O(n * 4) * 3
# Space Complexity - O(n) + O(n * 4)


def max_points_memo(arr, day, last, dp):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, arr[day][task])
        return maxi
    if dp[day][last] != -1:
        return dp[day][last]
    maxi = 0
    for task in range(3):
        if task != last:
            val = arr[day][task] + max_points_memo(arr, day - 1, task, dp)
            maxi = max(maxi, val)
    dp[day][last] = maxi
    return dp[day][last]

# Tabulation method : Bottom - Up Approach
# Time Complexity - O(n * 4) * 3
# Space Complexity - O(n * 4)


def get_max_points_tabulation(n, arr):
    dp = [[-1 for j in range(4)] for i in range(n)]
    dp[0][0] = max(arr[0][1], arr[0][2])
    dp[0][1] = max(arr[0][0], arr[0][2])
    dp[0][2] = max(arr[0][0], arr[0][1])
    dp[0][3] = max(arr[0][:])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if last != task:
                    val = arr[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], val)
    return dp[n - 1][3]


# Tabulation method - Optimised space
# Time Complexity - O(n * 4) * 3
# Space Complexity - O(4) * n


def get_max_points_space_optimised(n, arr):
    prev = [0] * 4
    prev[0] = max(arr[0][1], arr[0][2])
    prev[1] = max(arr[0][0], arr[0][2])
    prev[2] = max(arr[0][0], arr[0][1])
    prev[3] = max(arr[0][:])

    for day in range(1, n):
        temp = [0] * 4
        for last in range(4):
            temp[last] = 0
            for task in range(3):
                if last != task:
                    temp[last] = max(temp[last], arr[day][task] + prev[task])
        prev = temp
    return prev[3]


def get_max_points_memo(n, points):
    dp = [[-1 for j in range(4)] for i in range(n)]
    return max_points_memo(points, len(points) - 1, len(points[0]), dp)


if __name__ == "__main__":
    points = [
        [10, 40, 70],
        [20, 50, 80],
        [30, 60, 90]
    ]
    n = len(points)

    # Recursion
    print(max_points_recur(points, n - 1, len(points[0])))

    # Memoization
    print(get_max_points_memo(n, points))

    # Tabulation
    print(get_max_points_tabulation(n, points))

    # Space Optimized
    print(get_max_points_space_optimised(n, points))

