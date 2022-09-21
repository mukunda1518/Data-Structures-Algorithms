# Leetcode: https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Apporach1 : nlog(n)
        n = len(nums)
        l, r = 1, n - 1 
        while l < r:
            mid = l + (r - l) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1 
            if count <= mid:
                l = mid + 1 
            else:
                r = mid 
        return l
    
        # Apporach2 o(n)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow