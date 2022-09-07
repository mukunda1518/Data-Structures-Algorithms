# Leetcode: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

def is_min_len_possible(nums, n, min_len, k):
    # print(min_len)
    curr_sum = 0
    for i in range(min_len):
        curr_sum += nums[i]
    if curr_sum >= k:
        return True
    for i in range(min_len, n):
        curr_sum = curr_sum - nums[i - min_len] + nums[i]
        if curr_sum >= k:
            return True
    return False


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    l, r = 1, n
    min_len = 0
    while l <= r:
        mid = l + (r - l) // 2
        if is_min_len_possible(nums, n, mid, k):
            min_len = mid
            r = mid - 1
        else:
            l = mid + 1
    print(min_len)
