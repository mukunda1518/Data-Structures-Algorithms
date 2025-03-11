
# Leetcode: https://leetcode.com/problems/largest-rectangle-in-histogram/



# Youtube - https://www.youtube.com/watch?v=zx5Sw9130L0
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = [] # pair of (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (n - i))
        return max_area

            
# Youtube: https://www.youtube.com/watch?v=X0X6G-eWgQ8

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        max_area = 0
        left_small = []
        right_small = [0] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                left_small.append(0)
            else:
                left_small.append(stack[-1] + 1)
            stack.append(i)
    
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                right_small[i] = n - 1
            else:
                right_small[i] = stack[-1] - 1
            stack.append(i)

        for i in range(n):
            max_area = max(max_area, heights[i] * (right_small[i] - left_small[i] + 1))
    
        return max_area      
        