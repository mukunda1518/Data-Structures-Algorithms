def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    if nums[l] > target:
        return -1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            l = mid - 1
        else:
            r = mid + 1
    return r

# Return smallest num <= target
if __name__ == "__main__":
    nums = input().split(" ")
    target = int(input())
    nums = list(map(int, nums))
    print(binary_search(nums, target))