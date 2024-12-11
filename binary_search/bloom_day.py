# Leetcode: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/


class Solution:
    def is_bouquets_possible(self, bloomDay, day, m, k):
        no_of_bouquets = 0
        count = 0
        for b_day in bloomDay:
            if b_day <= day:
                count += 1
            else:
                no_of_bouquets += count // k
                count = 0
        no_of_bouquets += count // k
        return no_of_bouquets >= m

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        len_ = len(bloomDay)
        if len_ < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = low + (high - low) // 2
            if self.is_bouquets_possible(bloomDay, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1
        return low
