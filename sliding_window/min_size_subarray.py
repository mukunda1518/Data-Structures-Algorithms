# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # works for negative numbers also
        prefix_sum = 0
        res = float("inf")
        prefix_map = {0: -1} # to handle subarrays starts from 0 index
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - target in prefix_map:
                start_idx = prefix_map[prefix_sum - target]
                res = min(res, i - start_idx)
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        return 0 if res == float("inf") else res



        ## below works for only positive numbers
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res