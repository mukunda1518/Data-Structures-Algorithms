class Solution:

    def max_non_adj_sum(self, nums):
        prev1 = nums[0]
        prev2 = 0
        for i in range(1, len(nums)):
            take = nums[i] + prev2
            non_take = 0 + prev1
            prev2 = prev1
            prev1 = max(take, non_take)
        return prev1

    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.max_non_adj_sum(nums[1:]), self.max_non_adj_sum(nums[:-1]))
