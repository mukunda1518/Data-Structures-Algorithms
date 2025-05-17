# Count partitions with given difference

# Given an array arr of n integers and an integer diff, count the number of ways to partition the array into two subsets 
# such that the absolute difference between their sums is equal to diff. Return the result modulo 109+7.


# Example

# Input: arr = [1, 1, 2, 3], diff = 1

# Output: 3

# Explanation: The subsets are [1, 2] and [1, 3], [1, 3] and [1, 2], [1, 1, 2] and [3].


# https://www.youtube.com/watch?v=zoilQD1kYSg


# TC - O(2^n)
# SC - O(n)
def count_sum_k_recurr(idx, arr, k):
    if idx == 0:
        if k == 0 and arr[0] == 0:
            return 2  # {} and {0}
        if k == 0 or arr[0] == k:
            return 1
        return 0

    not_take = count_sum_k_recurr(idx - 1, arr, k)
    take = 0
    if arr[idx] <= k:
        take = count_sum_k_recurr(idx - 1, arr, k - arr[idx])
    return take + not_take

# TC - O(n * k)
 # SC - O(n * k) + O(n)
def count_sum_k_memo(idx, arr, k, dp):
    if idx == 0:
        if k == 0 and arr[0] == 0:
            return 2
        if k == 0 or arr[0] == k:
            return 1
        return 0

    if dp[idx][k] != -1:
        return dp[idx][k]

    not_take = count_sum_k_memo(idx - 1, arr, k, dp)
    take = 0
    if arr[idx] <= k:
        take = count_sum_k_memo(idx - 1, arr, k - arr[idx], dp)
    
    dp[idx][k] = take + not_take
    return dp[idx][k]


# TC - O(n * k)
# SC - O(n * k) 
def count_sum_k_tabu( arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base cases
    dp[0][0] = 2 if arr[0] == 0 else 1  # {} and {0} if arr[0] == 0, else just {}

    if arr[0] != 0 and arr[0] <= k:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for s in range(0, k + 1):
            not_take = dp[i - 1][s]
            take = 0
            if arr[i] <= s:
                take = dp[i - 1][s - arr[i]]
            dp[i][s] = take + not_take

    return dp[n - 1][k]

# TC - O(n * k)
# SC - O(k) 
def count_sum_k_space(arr, k):
    n = len(arr)
    prev = [0] * (k + 1)

    # Base case
    if arr[0] == 0:
        prev[0] = 2  # {} and {0}
    else:
        prev[0] = 1

    if arr[0] != 0 and arr[0] <= k:
        prev[arr[0]] = 1

    for i in range(1, n):
        curr = [0] * (k + 1)
        for s in range(0, k + 1):
            not_take = prev[s]
            take = 0
            if arr[i] <= s:
                take = prev[s - arr[i]]
            curr[s] = take + not_take
        prev = curr

    return prev[k]


if __name__ == "__main__":
    
    arr = [5, 2, 6, 4]
    D = 3
    total_sum = sum(arr)
    # s1 = sebset1
    # s2 = subset2
    # total_sum = s1_sum + s2+sum
    # s1_sum = total_sum - s2_sum
    # condition -> s1_sum - s2_sum = D
    # total_sum - s2_sum - s2_sum = D
    # s2_sum = (total_sum - D) // 2
    
    if total_sum - D < 0 or (total_sum - D) % 2 == 1:
        print(False)
    else:
        s2_sum = (total_sum - D) // 2
        print(count_sum_k_space(arr, s2_sum))

    
    
    
    