# Problem: https://www.codingninjas.com/codestudio/problems/house-robber_839733
# Solution: https://www.youtube.com/watch?v=3WaxQMELSkw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=7


# This problem is same as max sum of non adjacent elements from an array


# Tabulation method - Optimised space
# Time Complexity - O(n)
# Space Complexity - O(1)


def max_sum_space_optimized(nums):
    n = len(nums)
    prev = nums[0]
    prev1 = 0

    for i in range(1, n):
        take = nums[i] + prev1
        non_take = 0 + prev
        prev1 = prev
        prev = max(take, non_take)
    return prev


if __name__ == "__main__":
    n = 9
    nums = [1, 2, 3, 1, 3, 5, 8, 1, 9]

    # As the array is circular  first and last elements are adjacent

    # Leave the first element and find max_sum
    res1 = max_sum_space_optimized(nums[1:])

    # Leave the last element and find max_sum

    res2 = max_sum_space_optimized(nums[0:-1])

    print(max(res1, res2))
