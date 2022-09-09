# Leetcode Link: https://leetcode.com/problems/maximum-score-from-removing-stones/

import heapq


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:

        # Apporoach 1
        nums = [a, b, c]
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return nums[0] + nums[1]
        else:
            return nums[2] + (nums[0] + nums[1] - nums[2]) // 2

        # Approach 2
        min_heap = [-a, -b, -c]
        heapq.heapify(min_heap)
        count = 0
        while len(min_heap) > 1:
            max1 = -1 * heapq.heappop(min_heap) - 1
            max2 = -1 * heapq.heappop(min_heap) - 1
            if max1 > 0:
                heapq.heappush(min_heap, -max1)
            if max2 > 0:
                heapq.heappush(min_heap, -max2)
            count += 1
        return count