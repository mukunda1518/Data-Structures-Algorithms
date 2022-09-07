# Leetcode : https://leetcode.com/problems/employee-free-time/


import heapq


def get_free_times(intervals):
    heapq.heapify(intervals)
    res = []

    prev_end = intervals[0][1]
    heapq.heappop(intervals)
    while intervals:
        curr_start, curr_end = heapq.heappop(intervals)
        if curr_start > prev_end:
            res.append([prev_end, curr_start])
        prev_end = max(prev_end, curr_end)
    return res


if __name__ == "__main__":
    n = int(input())
    intervals = []
    for _ in range(n):
        list_ = [int(i) for i in input().split()]
        i = 0
        while i < len(list_) - 1:
            intervals.append((list_[i], list_[i + 1]))
            i += 2
    res = get_free_times(intervals)
    if res:
        for i in res:
            print(i[0], i[1])
    else:
        print(-1)
