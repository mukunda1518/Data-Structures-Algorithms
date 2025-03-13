# Leetcode: https://leetcode.com/problems/hand-of-straights/
# https://www.youtube.com/watch?v=amnrMCVd2YI

import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for num in range(first, first + groupSize):
                if num not in count:
                    return False
                count[num] -= 1

                if count[num] == 0:
                    if num != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True

