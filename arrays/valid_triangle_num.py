# Leetcode: https://leetcode.com/problems/valid-triangle-number/description/



# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



def triangleNumber(nums):
        count = 0
        if len(nums) < 3:
            return 0
        nums.sort()
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count


if __name__ == "__main__":
    nums = [2, 6, 7, 8, 16, 21]
    print(triangleNumber(nums))