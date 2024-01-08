# Leetcode: https://leetcode.com/problems/find-the-highest-altitude/description/


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        points_arr = [0]
        for i, gain_val in enumerate(gain):
            point = points_arr[i] + gain_val
            points_arr.append(point)
        return max(points_arr)
