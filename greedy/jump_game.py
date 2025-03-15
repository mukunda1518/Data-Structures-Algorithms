
# leetcode: https://leetcode.com/problems/jump-game/description/

# Youtube: https://www.youtube.com/watch?v=Yan0cv2cLy8


class Solution:
    # Recurssive Approach
    def can_jump(self, nums, index):
        if index >= len(nums) - 1:
            return True
        if nums[index] == 0:
            return False
        
        for i in range(1, nums[index]):
            if self.can_jump(nums, index + 1):
                return True
        return False

    def canJump(self, nums: list[int]) -> bool:

        # Geerdy Approach1
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


        # Greedy Approach 2
        max_index = 0
        n = len(nums)
        for i in range(n):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
            if max_index > n:
                return True
        return True
