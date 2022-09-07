# Leetcode: https://leetcode.com/problems/peak-index-in-a-mountain-array/

def get_peak_index(nums, n):
    l, r = 0, n - 1
    if l == r:
        return l
    while l <= r:
        mid = l + (r - l) // 2
        # print(mid, nums[mid - 1], nums[mid], nums[mid + 1])
        if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == n - 1 or nums[mid] > nums[mid + 1]):
            return mid
        elif mid > 0 and nums[mid] < nums[mid - 1]:
            r = mid - 1
        elif nums[mid] < nums[mid + 1]:
            l = mid + 1


if __name__ == "__main__":
    n = int(input())
    nums = input().split()
    nums = list(map(int, nums))
    print(get_peak_index(nums, n))