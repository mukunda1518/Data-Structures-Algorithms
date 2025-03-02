# Leetcode: https://leetcode.com/problems/trapping-rain-water/

# https://www.youtube.com/watch?v=ZI2z5pq0TqA

# Time Complexity: O(n)
# Space Complexity: O(2n)



class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        sufix_max = [0] * n

        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], height[i])

        sufix_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            sufix_max[i] = max(sufix_max[i+1], height[i])

        water_units = 0
        for i in range(n):
            left_max = prefix_max[i]
            right_max = sufix_max[i]
            if height[i] < left_max and height[i] < right_max:
                water_units += min(left_max, right_max) - height[i]
        return water_units 
    
 
 # Space Complexity: O(1)
    
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        left_max, right_max = height[l], height[r]

        water_units = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                water_units += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                water_units += right_max - height[r]
        return water_units
