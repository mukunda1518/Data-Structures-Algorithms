# Leetcode: https://leetcode.com/problems/rearrange-array-elements-by-sign/


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        p_index, n_index = 0, 1
        for num in nums:
            if num > 0:
                res[p_index] = num
                p_index += 2
            else:
                res[n_index] = num
                n_index += 2
        return res



        