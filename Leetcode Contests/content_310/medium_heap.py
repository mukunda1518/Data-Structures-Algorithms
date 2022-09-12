# leetcode Question: https://leetcode.com/contest/weekly-contest-310/problems/divide-intervals-into-minimum-number-of-groups/

from heapq import heapify, heappop, heappush
class Solution:
    def minGroups(self, intervals) -> int:
        intervals.sort()
        heap = []
        heapify(heap)
        for s, e in intervals:
            if heap and heap[0] < s:
                heappop(heap)
            heappush(heap, e)
        return len(heap)