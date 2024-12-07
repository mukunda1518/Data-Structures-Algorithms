# Leetcode: https://leetcode.com/problems/koko-eating-bananas/


import math

class Solution:

    def calculate_hours(self, piles, mid):
        total_hrs = 0
        for pile in piles:
            total_hrs += math.ceil(pile / mid)
        return total_hrs

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_val = max(piles)
        res = max_val
        low, high = 1, max_val
        while low <= high:
            mid = low + (high - low) // 2
            total_hrs = self.calculate_hours(piles, mid)
            if total_hrs <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

        
