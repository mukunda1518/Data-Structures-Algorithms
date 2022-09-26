# Leetcode: https://leetcode.com/contest/weekly-contest-312/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        non_incre_arr = [1] * n
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                non_incre_arr[i] += non_incre_arr[i-1]
            
        non_decr_arr = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                non_decr_arr[i] += non_decr_arr[i+1]

        good_indexes = []
        for i in range(k, n - k):
            if non_incre_arr[i-1] >= k and non_decr_arr[i+1] >= k:
                good_indexes.append(i)
        return good_indexes
