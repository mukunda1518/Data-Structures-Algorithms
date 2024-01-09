class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = 0
        len_ = len(nums)
        for i in range(1, len_):
            r_sum += nums[i]
        
        i = 0
        while i < len_ - 1:
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
            r_sum -= nums[i+1]
            i += 1
        if l_sum == r_sum:
            return i
        else:
            return -1

