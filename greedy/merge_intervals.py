
# Leetcode: https://leetcode.com/problems/merge-intervals/

# https://www.youtube.com/watch?v=2JzRBPFYbKE&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=7


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        merged_intervals = []
        n = len(intervals)
        intervals.sort()
        temp_interval = intervals[0]

        for i in range(n):
            if intervals[i][0] <= temp_interval[1]:
                temp_interval[1] = max(temp_interval[1], intervals[i][1])
            else:
                merged_intervals.append(temp_interval)
                temp_interval = intervals[i]
        merged_intervals.append(temp_interval)
        return merged_intervals
            
