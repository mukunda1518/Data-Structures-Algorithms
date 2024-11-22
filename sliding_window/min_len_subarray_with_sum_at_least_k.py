# Leetcode: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
from collections import deque

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


nums = [2, 7, 3, -8, 4, 10, 14]
k = 12

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        res = float("inf")
        q = deque() # (prefix_sum, index)
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            if curr_sum >= k:
                res = min(res, r + 1)

            while q and curr_sum - q[0][0] >= k:
                prefix_sum, index = q.popleft()
                res = min(res, r - index)
            
            while q and q[-1][0] > curr_sum:
                q.pop()
            q.append((curr_sum, r))
        return -1 if res == float("inf") else res
                
                        