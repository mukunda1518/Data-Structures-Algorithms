# Leetcode: https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)
        # find out the first greater element
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index != -1:
            # swap the first greater element with num at index 
            for i in range(n-1, index, -1):
                if nums[i] > nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]
                    break

        # swap the elements after the index 
        l = index + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        