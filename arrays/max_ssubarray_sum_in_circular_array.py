# Leetcode: https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/

def max_subarray_sum_circular(nums, n):
    total = curr_max = curr_min = 0
    max_sum = min_sum = nums[0]
    for num in nums:
        curr_max = max(curr_max + num, num)
        max_sum = max(curr_max, max_sum)
        curr_min = min(curr_min + num, num)
        min_sum = min(min_sum, curr_min)
        total += num

    if max_sum > 0:
        result = max(max_sum, total - min_sum)
    else:
        result = max_sum
    return result


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(max_subarray_sum_circular(nums, n))

