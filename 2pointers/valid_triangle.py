# Leetcode: https://leetcode.com/problems/valid-triangle-number/

# Time Complexitiy - O(n^2)
# Space Complexity - O(1)


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(2, n):
            lp, hp = 0, i - 1
            while lp < hp:
                if nums[lp] + nums[hp] > nums[i]:
                    count += hp - lp
                    hp -= 1
                else:
                    lp += 1
        return count

if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    print(Solution().triangleNumber(nums))   
                