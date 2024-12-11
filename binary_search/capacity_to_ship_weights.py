# Leetcode: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:

    def get_no_of_days_to_ship_the_weights(self, weights, capacity):
        days = 0
        load = 0
        for weight in weights:
            if load + weight > capacity:
                days += 1
                load = weight
            else:
                load += weight
        return days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        maxi = max(weights)
        sum_ = sum(weights)
        low, high = maxi, sum_
        while low <= high:
            mid = low + (high - low) // 2
            no_of_days = self.get_no_of_days_to_ship_the_weights(weights, mid)
            if no_of_days <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low
 