# Leetcode: https://leetcode.com/problems/wiggle-sort/


def wiggle_sort(nums):
    n = len(nums)
    nums.sort()
    for i in range(1, n - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(*nums)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    wiggle_sort(nums)

