# Leetcode: https://leetcode.com/problems/non-overlapping-intervals/

# https://www.youtube.com/watch?v=HDHQ8lAWakY


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[1])
        last_end_time = intervals[0][1]
        n = len(intervals)
        count = 1
        for i in range(1, n):
            if intervals[i][0] >= last_end_time:
                count += 1
                last_end_time = intervals[i][1]
        return n - count

            


        