def peak_element(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return r # return l or r - both are same

if __name__ == "__main__":
    nums = input().split(" ")
    nums = list(map(int, nums))
    print(peak_element(nums))
    
    
# Peak Element: https://leetcode.com/problems/find-peak-element/
# Problem: https://www.youtube.com/watch?v=cXxmbemS6XM&t=1852s


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]: 
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        low, high = 1, n - 2

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                low = mid + 1
            elif nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
