# Leetcode: https://leetcode.com/problems/jump-game-ii/


# https://www.youtube.com/watch?v=dJ7sWiOoK7g
# https://www.youtube.com/watch?v=7SBVnw7GSTk



class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res        