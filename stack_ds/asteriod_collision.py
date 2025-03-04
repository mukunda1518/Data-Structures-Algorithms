# Leetcode: https://leetcode.com/problems/asteroid-collision/

# https://www.youtube.com/watch?v=_eYGqw_VDR4


# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.




class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:

            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()

                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
        return stack
