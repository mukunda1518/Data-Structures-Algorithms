# Leetcde: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

def min_no_of_swaps(nums, n):
    no_ones = nums.count(1)
    count, max_count = 0, 0
    i, j = 0, 0
    while j < n:
        while j < n and j - i < no_ones:
            if nums[j] == 1:
                count += 1
            j += 1
        max_count = max(max_count, count)
        if j == n:
            break
        if nums[i] == 1:
            count -= 1
        i += 1
    return no_ones - max_count


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(min_no_of_swaps(nums, n))