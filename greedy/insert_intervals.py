
# Leetcode: https://leetcode.com/problems/insert-interval/

# https://www.youtube.com/watch?v=xxRE-46OCC8



class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        n = len(intervals)
        # For non-overlaping left intervals 
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # For Overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)
        # For Non-overlapping right intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        return res

