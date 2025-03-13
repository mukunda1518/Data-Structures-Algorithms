# Leetcode: https://leetcode.com/problems/find-median-from-data-stream/

# https://www.youtube.com/watch?v=itmhHWaHupI


import heapq


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check for every num in small <= every num in large
        while self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            num = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        
        # check for uneven sizes
        if len(self.small) > len(self.large) + 1:
            num = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        
        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()