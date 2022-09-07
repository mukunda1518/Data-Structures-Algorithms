# LeetCode Problem Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import heapq


def smallest_range(nums):
    # Push first set of k elements in pq (0th index of all list)
    pq = [(row[0], i, 0) for i, row in enumerate(nums)]
    heapq.heapify(pq)

    cur_max = max(row[0] for row in nums)
    cur_range = 1e9

    while True:
        cur_min, row, index = heapq.heappop(pq)
        # Check new range is possible
        if cur_max - cur_min < cur_range:
            start = cur_min
            end = cur_max
            cur_range = cur_max - cur_min

        # If we run out elements in the list
        if index + 1 == len(nums[row]):
            return (start, end)
        val = nums[row][index + 1]

        # Update curr_max if newly added element is max
        cur_max = max(cur_max, val)
        heapq.heappush(pq, (val, row, index + 1))


if __name__ == "__main__":
    k = int(input())
    nums = []
    for _ in range(k):
        list_ = [int(val) for val in input().split()][1:]
        nums.append(list_)
    ans = smallest_range(nums)
    print(ans[0], ans[1])