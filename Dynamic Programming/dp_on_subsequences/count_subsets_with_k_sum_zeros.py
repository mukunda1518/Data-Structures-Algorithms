# when 0's are given 
# https://takeuforward.org/plus/dsa/problems/count-subsets-with-sum-k
# https://www.youtube.com/watch?v=ZHyb-A2Mte4



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
