# Leetcode: https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        len_ = len(nums)
        for i in range(len_ - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lp, hp, sum_ = i + 1, len_ - 1, -(nums[i]) 
                while lp < hp:
                    if nums[lp] + nums[hp] == sum_:
                        result.append([nums[i], nums[lp], nums[hp]])
                        while lp < hp and nums[lp] == nums[lp + 1]: lp += 1
                        while hp > lp and nums[hp] == nums[hp - 1]: hp -= 1
                        lp += 1
                        hp -= 1  
                    elif nums[lp] + nums[hp] < sum_:
                        lp += 1
                    else:
                        hp -= 1             
        return result

if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    print(Solution().threeSum(nums))

    